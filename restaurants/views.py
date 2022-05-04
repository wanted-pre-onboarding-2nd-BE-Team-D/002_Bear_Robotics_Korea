from django.http      import Http404
from datetime         import datetime,timedelta

from rest_framework          import status
from rest_framework.response import Response
from rest_framework.views    import APIView

from .models      import Restaurant, Subsidary, Menu, Ward, Neighborhood
from .serializers import SubsidarySerializer, RestaurantSerializer, MenuSerializer


# 업종정보 API CRUD

# Subsidary API
class SubsidaryList(APIView):
    """
        류성훈
    """
    def get(self, request, format = None):
        # Subsidary의 모든 유효한 데이터를 읽어온다.
        subsidary  = Subsidary.objects.filter(is_delete = False)
        serializer = SubsidarySerializer(subsidary, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Subsidary에 새로운 데이터를 추가합니다.
        serializer = SubsidarySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class SubsidaryDetail(APIView):
    """
        류성훈
    """
    def get_object(self, id):
        # 받아올 데이터의 유효성을 검사합니다.
        try:
            return Subsidary.objects.get(id = id)
        except Subsidary.DoesNotExist:
            raise Http404

    def get(self, request, id, format = None):
        subsidary  = self.get_object(id)
        serializer = SubsidarySerializer(subsidary)
        return Response(serializer.data)

    def put(self, request, id, format = None):
        subsidary  = self.get_object(id)
        serializer = SubsidarySerializer(subsidary, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # Soft Delete 방식 채택으로 인한 Delete기능 주석처리
    # def delete(self, request, id, format=None):
    #     subsidary = self.get_object(id)
    #     subsidary.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # 한번 삭제 시 Soft Delete / Soft Delete 된 데이터 또 삭제 시 영구 Delete
    def delete(self, request, id, format = None):
        try:
            subsidary = Subsidary.objects.get(id = id)
            if subsidary.is_delete == True:
                raise Subsidary.DoesNotExist
            serializer = SubsidarySerializer(subsidary)
            subsidary.is_delete = True
            subsidary.delete_at = datetime.now()
            subsidary.save()
            return Response(serializer, status = 200)
        except Subsidary.DoesNotExist:
            return Response(status = 404)


class RestaurantListCR(APIView):    
    """
    Restaurant List CR API
    
    김석재
    """
    
    def _change_to_id(self, request):
        # 주소, 업종을 id로 변환
        ward          = request.data['ward']
        subsidary     = request.data['subsidary']        
        ward_obj      = Ward.objects.get(name=ward)
        subsidary_obj = Subsidary.objects.get(name=subsidary)        
        return ward_obj, subsidary_obj ,ward ,subsidary
    
    def get(self, request,id = None):
        # 레스토랑 조회, search 쿼리가 들어오면 주소나, 이름중에 찾는다
        if request.GET['search']:
            obj     = Restaurant.objects.filter(name__icontains=request.GET['search'],
                                                    is_delete=False)
        else:
            obj     = Restaurant.objects.filter(is_delete=False)
        serializers = RestaurantSerializer(obj, many = False)
        return Response(serializers.data)

    def post(self, request,id = None):
        # 주소, 업종을 id로 변환
        ward_obj, subsidary_obj ,ward ,subsidary= self._change_to_id(request)
        store=request.data['store']
        
        # 주소와 업종, 호점 동시에 똑같은 값이 있을 경우 & 삭제되지않았을때
        try:
            if Restaurant.objects.get(ward_id = ward_obj.id, subsidary_id = subsidary_obj.id,
                                      store=store ,is_delete = False):
                return Response({'MESSAGE': 'DUPLICATE_VALUE'}, status = 400)
        except:
            create_obj       = Restaurant.objects.create(
                ward_id      = ward_obj.id,
                subsidary_id = subsidary_obj.id,
                store        = store,
                name         = f"{subsidary}, {ward}점"
            )
        
        serializers = RestaurantSerializer(create_obj)
        return Response(serializers.data)    
    
class RestaurantListUD(APIView):    
    """
    Restaurant List UD API
    
    김석재
    """
    def _change_to_id(self, request):
        # 주소, 업종을 id로 변환
        ward          = request.data['ward']
        subsidary     = request.data['subsidary']        
        ward_obj      = Ward.objects.get(name=ward)
        subsidary_obj = Subsidary.objects.get(name=subsidary)        
        return ward_obj, subsidary_obj
    
    def get(self, request,id = None):
        # Restaurant 디테일 조회        
        obj  = Restaurant.objects.get(is_delete=False, id=id)      
        serializers = RestaurantSerializer(obj, many = True)
        return Response(serializers.data)
    
    def put(self, request,id = None):
        if id:
            if len(request.data.values()) == 0:
                raise ValueError("MISSING_VALUE")

            ward_obj, subsidary_obj ,ward ,subsidary = self._change_to_id(request)
            obj = Restaurant.objects.get(id = id)            

            # 삭제된 값이라면 에러
            if obj.is_delete == True:
                raise ValueError("DOES_NOT_EXIST")

            # 입력된 값을 변경
            if 'ward' in request.data:
                obj.ward_id      = ward_obj.id
            if 'subsidary' in request.data:
                obj.subsidary_id = subsidary_obj.id
            if 'store' in request.data:
                obj.store        = request.data['store']

            # 주소와 업종 동시에 똑같은 값이 있을 경우
            try:
                if Restaurant.objects.get(ward_id = obj.ward_id, subsidary_id = obj.subsidary_id,
                                          store = obj.store, is_delete = False):
                    return Response({'MESSAGE': 'DUPLICATE_VALUE'}, status = 400)
            except:
                obj.name = f"{subsidary}, {ward}점"
                obj.save()
        else:
            raise ValueError("MISSING_VALUE")
        serializers = RestaurantSerializer(obj)
        return Response(serializers.data)

    def delete(self, request,id = None):
        if id:
            obj = Restaurant.objects.get(id = id)
            
            # 이미 삭제 되었다면 에러
            if obj.is_delete == True:
                raise ValueError("DOES_NOT_EXIST")
            else:
                obj.is_delete = True
                obj.delete_at = datetime.now()
            obj.save()
        else:
            # ID입력을 안하면 에러
            raise ValueError("MISSING_VALUE")
        
        serializers = RestaurantSerializer(obj)
        return Response(serializers.data)
    

class MenuCreateListView(APIView):
    """
        정미정

        {
         "subsidary": 1 // subsidary_id
         "name": "menu1",
         "price": 10000
         }
    """

    def get(self, request):
        menus = Menu.objects.filter(is_delete=False)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetailView(APIView):
    """
        정미정
    """

    def get_object(self, id):
        try:
            return Menu.objects.get(id=id)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        menu = self.get_object(id)
        if menu.status_code == 404:
            return Response({'MESSAGE': 'MENU_DOES_NOT_EXIST'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(menu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        menu = self.get_object(id)
        if menu.status_code == 404:
            return Response({'MESSAGE': 'MENU_DOES_NOT_EXIST'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(menu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        menu = self.get_object(id)

        if menu.status_code == 404 or menu.is_delete:
            return Response({'MESSAGE': 'MENU_DOES_NOT_EXIST'}, status=status.HTTP_404_NOT_FOUND)

        menu.is_delete = True
        menu.delete_at = datetime.now()
        menu.save()
        return Response({'MESSAGE': 'SUCCESS'}, status=status.HTTP_200_OK)
