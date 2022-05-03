from itertools        import count
from logging          import exception
from urllib           import request
from django.http      import Http404
from django.shortcuts import render
from datetime         import datetime,timedelta

from rest_framework          import status
from rest_framework.response import Response
from rest_framework.views    import APIView

from .models      import Restaurant, Subsidary, Menu, Ward, Neighborhood
from .serializers import SubsidarySerializer, RestaurantSerializer
from restaurants  import serializers


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
        serializer = SubsidarySerializer(darta = request.data)
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

#레스토랑 API
class RestaurantAPI(APIView):
    """
    김석재
    """

    # 주소, 업종을 id로 변환
    def chang_to_id(self, request):
        ward          = request.data['ward']
        subsidary     = request.data['subsidary']
        ward_obj      = Ward.objects.get(name=ward)
        subsidary_obj = Subsidary.objects.get(name=subsidary)
        return ward_obj, subsidary_obj

    # Restaurant 조회
    def get(self, request,id = None):        
        many = True
        # id 쿼리를 받으면 부분 조회
        if id:
            obj  = Restaurant.objects.get(is_delete=False, id=id)
            many = False
        else:
            obj     = Restaurant.objects.filter(is_delete=False)
        serializers = RestaurantSerializer(obj, many = many)
        return Response(serializers.data)

    def post(self, request,id = None):
        # 주소, 업종을 id로 변환
        ward_obj, subsidary_obj = self.chang_to_id(request)
        print(ward_obj.id, subsidary_obj.id)

        # 주소와 업종 동시에 똑같은 값이 있을 경우 & 삭제되지않았을때
        try:
            if Restaurant.objects.get(ward_id = ward_obj.id, subsidary_id = subsidary_obj.id, is_delete = False):
                return Response({'MESSAGE': 'DUPLICATE_VALUE'}, status = 400)
        except:                    
            create_obj       = Restaurant.objects.create(
                ward_id      = ward_obj.id,
                subsidary_id = subsidary_obj.id,                
            )
        #create_obj.save()
        serializers = RestaurantSerializer(create_obj)
        return Response(serializers.data)

    def put(self, request,id = None):
        if id:
            if len(request.data.values()) == 0:
                raise ValueError("MISSING_VALUE")

            ward_obj, subsidary_obj = self.chang_to_id(request)
            obj = Restaurant.objects.get(id = id)

            # 삭제된 값이라면 에러
            if obj.is_delete == True:
                raise ValueError("DOES_NOT_EXIST")

            # 입력된 값을 변경
            if 'ward' in request.data:
                obj.ward_id      = ward_obj.id
            if 'subsidary' in request.data:
                obj.subsidary_id = subsidary_obj.id

            # 주소와 업종 동시에 똑같은 값이 있을 경우
            try:
                if Restaurant.objects.get(ward_id = obj.ward_id, subsidary_id = obj.subsidary_id, is_delete = False):
                    return Response({'MESSAGE': 'DUPLICATE_VALUE'}, status = 400)
            except:
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
