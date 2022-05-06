from urllib import response
from django.http import Http404
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant, Subsidary, Menu, Ward, Neighborhood
from .serializers import SubsidarySerializer, RestaurantSerializer, MenuSerializer


# 업종정보 API CRUD

# Subsidary API
class SubsidaryList(APIView):
    """
        류성훈
    """

    def get(self, request, format=None):
        # Subsidary의 모든 유효한 데이터를 읽어온다.
        subsidary = Subsidary.objects.filter(is_delete=False)
        serializer = SubsidarySerializer(subsidary, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Subsidary에 새로운 데이터를 추가합니다.
        serializer = SubsidarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubsidaryDetail(APIView):
    """
        류성훈
    """

    def get_object(self, id):
        # 받아올 데이터의 유효성을 검사합니다.
        try:
            return Subsidary.objects.get(id=id)
        except Subsidary.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        subsidary = self.get_object(id)
        serializer = SubsidarySerializer(subsidary)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        subsidary = self.get_object(id)
        serializer = SubsidarySerializer(subsidary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Soft Delete 방식 채택으로 인한 Delete기능 주석처리
    # def delete(self, request, id, format=None):
    #     subsidary = self.get_object(id)
    #     subsidary.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # 한번 삭제 시 Soft Delete / Soft Delete 된 데이터 또 삭제 시 영구 Delete
    def delete(self, request, id, format=None):
        try:
            subsidary = Subsidary.objects.get(id=id)
            if subsidary.is_delete == True:
                raise Subsidary.DoesNotExist
            serializer = SubsidarySerializer(subsidary)
            subsidary.is_delete = True
            subsidary.delete_at = datetime.now()
            subsidary.save()
            return Response(serializer, status=200)
        except Subsidary.DoesNotExist:
            return Response(status=404)


class RestaurantListCR(APIView):
    """
    Restaurant List CR API

    김석재
    """

    def _get_values(self, request):
        values = {
            'store': request.data.get('store', None),
            'ward': request.data.get('ward', None),
            'subsidary': request.data.get('subsidary', None),
        }
        return values

    def _change_to_id(self, values):
        values['ward_id'] = Ward.objects.get(name=values['ward']).id
        values['subsidary_id'] = Subsidary.objects.get(name=values['subsidary']).id

        return values

    def get(self, request):
        """
        GET: restaurant
        GET: restaurant?search=something
        레스토랑 조회, search 쿼리가 들어오면 주소나, 이름중에 찾는다
        """

        if 'search' in request.GET:
            obj = Restaurant.objects.filter(name__icontains=request.GET['search'],
                                            is_delete=False)
        else:
            obj = Restaurant.objects.filter(is_delete=False)
        serializers = RestaurantSerializer(obj, many=True)
        return Response(serializers.data)

    def post(self, request):
        """
        POST: resurant
        data: {
                "subsidary" : "맥도날드",
                "ward"      : "서초구 서초동",
                "store"     : 1
            }
        값을 입력받아 생성
        """

        # 주소, 업종을 id로 변환
        values = self._get_values(request)
        if None in values.values():
            return Response({'MESSAGE': 'MISSING_VALUE'}, status=400)
        if "" in values.values():
            return Response({'MESSAGE': 'MISSING_VALUE'}, status=400)
        values = self._change_to_id(values=values)

        # 주소와 업종, 호점 동시에 똑같은 값이 있을 경우 & 삭제되지않았을때
        try:
            if Restaurant.objects.get(ward_id=values['ward_id'], subsidary_id=values['subsidary_id'],
                                      store=values['store'], is_delete=False):
                return Response({'MESSAGE': 'DUPLICATE_VALUE'}, status=400)
        except:
            create_obj = Restaurant.objects.create(
                ward_id=values['ward_id'],
                subsidary_id=values['subsidary_id'],
                store=values['store'],
                name=f"{values['subsidary']}, {values['ward']}점"
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
        values = {}
        values['ward'] = request.data['ward']
        values['subsidary'] = request.data['subsidary']
        values['ward_obj'] = Ward.objects.get(name=values['ward'])
        values['subsidary_obj'] = Subsidary.objects.get(name=values['subsidary'])
        return values

    def get(self, request, id=None):
        """
        GET: restaurant/<id>
        디테일 조회
        """
        try:
            obj = Restaurant.objects.get(is_delete=False, id=id)
        except:
            return Response({'MESSAGE': 'DOES_NOT_EXIST'}, status=404)
        serializers = RestaurantSerializer(obj, many=False)
        return Response(serializers.data)

    def put(self, request, id=None):
        """
        PUT: restaurant/<id>
        data:{
                "subsidary" : "맥도날드",
                "ward"      : "서초구 서초동",
                "store"     : 1
            }
        값을 입력받아 수정
        """

        if id:
            if len(request.data.values()) == 0 or "" in request.data.values():
                return Response({'MESSAGE': 'MISSING_VALUE'}, status=400)

            obj = Restaurant.objects.get(id=id)

            # 삭제된 값이라면 에러
            if obj.is_delete == True:
                Response({'MESSAGE': 'DOES_NOT_EXIST'}, status=404)

            # 입력된 값을 변경
            if 'ward' in request.data:
                ward_obj = Ward.objects.get(name=request.data['ward'])
                obj.ward_id = ward_obj.id
            if 'subsidary' in request.data:
                subsidary_obj = Subsidary.objects.get(name=request.data['subsidary'])
                obj.subsidary_id = subsidary_obj.id
            if 'store' in request.data:
                obj.store = request.data['store']

            # 주소와 업종 동시에 똑같은 값이 있을 경우
            try:
                if Restaurant.objects.get(ward_id=obj.ward_id, subsidary_id=obj.subsidary_id,
                                          store=obj.store, is_delete=False):
                    return Response({'MESSAGE': 'DUPLICATE_VALUE'}, status=400)
            except:
                ward = Ward.objects.get(id=obj.ward_id).name
                subsidary = Subsidary.objects.get(id=obj.subsidary_id).name
                obj.name = f"{subsidary}, {ward}점"
                obj.save()
        else:
            Response({'MESSAGE': 'MISSING_VALUE'}, status=400)
        serializers = RestaurantSerializer(obj)

        return Response(serializers.data)

    def delete(self, request, id=None):
        if id:
            obj = Restaurant.objects.get(id=id)

            # 이미 삭제 되었다면 에러
            if obj.is_delete == True:
                Response({'MESSAGE': 'DOES_NOT_EXIST'}, status=404)
            else:
                obj.is_delete = True
                obj.delete_at = timezone.localtime()
            obj.save()
        else:
            # ID입력을 안하면 에러
            Response({'MESSAGE': 'MISSING_VALUE'}, status=400)

        serializers = RestaurantSerializer(obj)
        return Response(serializers.data)


class RestaurantListUD(APIView):
    """
    Restaurant List UD API

    김석재
    """

    def _change_to_id(self, request):
        # 주소, 업종을 id로 변환
        values = {}
        values['ward'] = request.data['ward']
        values['subsidary'] = request.data['subsidary']
        values['ward_obj'] = Ward.objects.get(name=values['ward'])
        values['subsidary_obj'] = Subsidary.objects.get(name=values['subsidary'])
        return values

    def get(self, request, id=None):
        """
        GET: restaurant/<id>
        디테일 조회
        """
        try:
            obj = Restaurant.objects.get(is_delete=False, id=id)
        except:
            return Response({'MESSAGE': 'DOES_NOT_EXIST'}, status=404)
        serializers = RestaurantSerializer(obj, many=False)
        return Response(serializers.data)

    def put(self, request, id=None):
        """
        PUT: restaurant/<id>
        data:{
                "subsidary" : "맥도날드",
                "ward"      : "서초구 서초동",
                "store"     : 1
            }
        값을 입력받아 수정
        """

        if id:
            if len(request.data.values()) == 0 or "" in request.data.values():
                return Response({'MESSAGE': 'MISSING_VALUE'}, status=400)

            obj = Restaurant.objects.get(id=id)

            # 삭제된 값이라면 에러
            if obj.is_delete == True:
                Response({'MESSAGE': 'DOES_NOT_EXIST'}, status=404)

            # 입력된 값을 변경
            if 'ward' in request.data:
                ward_obj = Ward.objects.get(name=request.data['ward'])
                obj.ward_id = ward_obj.id
            if 'subsidary' in request.data:
                subsidary_obj = Subsidary.objects.get(name=request.data['subsidary'])
                obj.subsidary_id = subsidary_obj.id
            if 'store' in request.data:
                obj.store = request.data['store']

            # 주소와 업종 동시에 똑같은 값이 있을 경우
            try:
                if Restaurant.objects.get(ward_id=obj.ward_id, subsidary_id=obj.subsidary_id,
                                          store=obj.store, is_delete=False):
                    return Response({'MESSAGE': 'DUPLICATE_VALUE'}, status=400)
            except:
                ward = Ward.objects.get(id=obj.ward_id).name
                subsidary = Subsidary.objects.get(id=obj.subsidary_id).name
                obj.name = f"{subsidary}, {ward}점"
                obj.save()
        else:
            Response({'MESSAGE': 'MISSING_VALUE'}, status=400)
        serializers = RestaurantSerializer(obj)

        return Response(serializers.data)

    def delete(self, request, id=None):
        if id:
            obj = Restaurant.objects.get(id=id)

            # 이미 삭제 되었다면 에러
            if obj.is_delete == True:
                Response({'MESSAGE': 'DOES_NOT_EXIST'}, status=404)
            else:
                obj.is_delete = True
                obj.delete_at = timezone.localtime()
            obj.save()
        else:
            # ID입력을 안하면 에러
            Response({'MESSAGE': 'MISSING_VALUE'}, status=400)

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
        subsidary = request.data['subsidary']
        name = request.data['name']
        if Menu.objects.get(subsidary_id=subsidary, name=name, is_delete=False):
            return Response({'MESSAGE': 'DUPLICATE_VALUE'}, status=400)

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
        if menu == 404:
            return Response({'MESSAGE': 'MENU_DOES_NOT_EXIST'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(menu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        menu = self.get_object(id)
        if menu == 404:
            return Response({'MESSAGE': 'MENU_DOES_NOT_EXIST'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(menu, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        menu = self.get_object(id)

        if menu == 404 or menu.is_delete:
            return Response({'MESSAGE': 'MENU_DOES_NOT_EXIST'}, status=status.HTTP_404_NOT_FOUND)

        menu.is_delete = True
        menu.delete_at = datetime.now()
        menu.save()
        return Response({'MESSAGE': 'SUCCESS'}, status=status.HTTP_200_OK)
