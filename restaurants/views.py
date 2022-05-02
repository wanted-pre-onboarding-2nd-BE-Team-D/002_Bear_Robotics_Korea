from django.http import Http404
from django.shortcuts import render

from datetime                  import datetime,timedelta

from rest_framework            import status
from rest_framework.response   import Response
from rest_framework.views      import APIView

from .models                   import Restaurant,Subsidary,Menu,Ward,Neighborhood
from .serializers              import SubsidarySerializer
from restaurants import serializers
# Create your views here.

# 업종정보 API CRUD
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
                subsidary.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            serializer = SubsidarySerializer(subsidary)
            subsidary.is_delete = True
            subsidary.delete_at = datetime.now()
            subsidary.save()
            return Response(serializer, status=200)

        except Subsidary.DoesNotExist:
            return Response(status=404)

        
