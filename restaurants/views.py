from urllib import request
from django.http import Http404
from django.shortcuts import render

from rest_framework            import status
from rest_framework.response   import Response
from rest_framework.views      import APIView

from .models                   import Restaurant,Subsidary,Menu,Ward,Neighborhood
from .serializers              import SubsidarySerializer,RestaurantSerializer
from restaurants import serializers
# Create your views here.

# 업종정보 API CRUD
class SubsidaryList(APIView):
    """
    류성훈
    """
    def get(self, request, format=None):
        # Subsidary의 모든 데이터를 읽어온다.
        subsidary = Subsidary.objects.all()
        serializer = SubsidarySerializer(subsidary, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Subsidary에 새로운 데이터를 추가합니다.
        serializer = SubsidarySerializer(darta=request.data)
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

    def delete(self, request, id, format=None):
        subsidary = self.get_object(id)
        subsidary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RestaurantAPI(APIView):
    #Restaurant 조회
    def get(self,request): 
        many=True     
        #id 쿼리를 받으면 부분 조회
        if 'id' in request.GET:
            obj=Restaurant.objects.get(is_delete=False,id=request.GET['id'])        
            many=False    
        else:
            obj=Restaurant.objects.filter(is_delete=False)
        serializers = RestaurantSerializer(obj,many=many)
        return Response(serializers.data)
    
    def post(self,request):
        #주소, 업종을 id로 변환
        ward=request.data['ward']
        subsidary=request.data['subsidary']      
        ward_obj=Ward.objects.get(name=ward)
        subsidary_obj=Subsidary.objects.get(name=subsidary)
        
        #주소와 업종 동시에 똑같은 값이 있을 경우
        if Restaurant.objects.get(ward_id=ward_obj.id,subsidary_id=subsidary_obj.id):                
            raise ValueError("중복된 값이 있습니다")        
            
        create_obj=Restaurant.objects.create(
            ward_id=ward_obj.id,
            subsidary_id=subsidary_obj.id
        )
        serializers = RestaurantSerializer(create_obj)
        return Response(serializers.data)
    
    def put(self,request):        
        if 'id' in request.PUT:
            obj=Restaurant.objects.get(id=request.PUT['id'])
            if 'ward' in request.PUT:
                obj.ward_id= request.PUT['ward']
            if 'subsidary' in request.PUT:
                obj.subsidary_id= request.PUT['subsidary']
            #주소와 업종 동시에 똑같은 값이 있을 경우
            if Restaurant.objects.get(ward_id=obj.ward_id,subsidary_id=obj.subsidary_id):                
                raise ValueError("중복된 값이 있습니다")                   
            obj.save()                    
        else :
            raise
        serializers = RestaurantSerializer(obj)
        return Response(serializers.data)
 
        