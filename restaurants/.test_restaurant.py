import json
import pytest
import random

from datetime            import datetime
from django.test         import TestCase, Client
from django.urls         import reverse
from rest_framework      import status
from rest_framework.test import APITestCase

from restaurants.models  import Restaurant,Subsidary,Menu,Ward,Neighborhood
from restaurants         import views



@pytest.mark.django_db()
class TestViewRestaurant:
    """
    김석재
    """

  # fixture 매 test마다 반복됨
    @pytest.fixture
    def set_user(self, client):
        User.objects.create(
            advertiser = "37445221"
        )
        self.data = {
            "advertiser_id" : "37445221",
            "media"         : "naver",
            "start_date"    : "2022-04-30",
            "end_date"      : "2022-05-30",
            "uid"           : "1819",            
        }
        
    @pytest.fixture
    def set_for_result(self, client,set_user):
        self.create_post(client, set_user)
        obj_list = Result.objects.all()           
        for obj in obj_list:
            obj.cost       = 100
            obj.impression = 100
            obj.click      = 1000
            obj.conversion = 100
            obj.cv         = 10
            obj.save()    
    
    #반복되는 post     
    def create_post(self,client,set_user):
        response = client.post(
            reverse(views.post_create_ad),
            data = self.data
        )
        return response
    
    # 반복되는 조회
    def read_result(self, client, set_user,set_for_result):
        response = client.get('/advertise/result/?advertiser=37445221&start_date=2022-04-30&end_date=2022-05-30')
        return response
    
    #POST가 아닌 요청(GET사용)
    def test_create_get(self, client, set_user):
        response = client.get(reverse(views.post_create_ad))             
        assert response.status_code == 405
        assert response.json()      == {'detail': 'Method "GET" not allowed.'}
        

    # 필수 값
    def test_create_ad(self, client, set_user):        
        response = self.create_post(client, set_user)        
        assert response.status_code   == 200
        assert Ad.objects.count()     == 1
        assert Result.objects.count() == 31
    
    # 필수 값 + 선택 값
    def test_create_ad_with_more_value(self, client, set_user):
        self.data['estimated_spend']  = "11.1"
        self.data['budget']           = "11.5"
        response = self.create_post(client, set_user) 
        assert response.status_code   == 200
        assert Ad.objects.count()     == 1
        assert Result.objects.count() == 31

    # 필수 값이 누락
    def test_create_ad_without_start_date(self, client, set_user):
        self.data['start_date'] = ""
        response = self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE': 'MISSING_VALUE'}

    def test_create_ad_without_end_date(self, client, set_user):
        self.data['end_date'] = ""
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE': 'MISSING_VALUE'}

    def test_create_ad_without_advertiser_id(self, client, set_user):
        self.data['advertiser_id'] = ""
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE': 'MISSING_VALUE'}

    def test_create_ad_without_media(self, client, set_user):
        self.data['media'] = ""
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE': 'MISSING_VALUE'}

    def test_create_ad_without_uid(self, client, set_user):
        self.data['uid'] = ""
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE': 'MISSING_VALUE'}
    
    # start_day가 오늘보다 전   
    def test_create_ad_with_invalid_start_date(self, client, set_user):
        self.data['start_date'] = "1500-01-15"
        response=self.create_post(client, set_user)        
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE': 'INVALID_DATE'}
    
    # end_day가 start_day보다 전 
    def test_create_ad_with_invalid_end_date(self, client, set_user):
        self.data['start_date'] = "2000-01-15"
        self.data['end_date']   = "2000-01-05"
        response=self.create_post(client, set_user)
       
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE': 'INVALID_DATE'}
        
    #budget 이 음수
    def test_create_ad_with_negative_budget(self, client, set_user):
        self.data['budget'] = "-1"
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE': 'INVALID_VALUE'}
    
    #estimated_spend 가 음수
    def test_create_ad_with_negative_estimated_spend(self, client, set_user):
        self.data['estimated_spend'] = "-1"
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE': 'INVALID_VALUE'}
        
    # Read  
    # advertiser , start_date, end_date 미입력
    def test_read_without_values(self,client,set_user):
        response=client.get(reverse(views.get_result))        
        assert response.status_code == 404
        assert response.json()      == '존재하지 않는 광고주 id입니다.'
    
    # advertiser , start_date, end_date 입력시 
    def test_read_with_values(self,client,set_user,set_for_result):    
        response=self.read_result(client,set_user,set_for_result)
        
        assert response.status_code == 200
        assert response.json()      == {'naver': {'ctr': 1000.0, 'roas': 10.0, 'cpc': 0.1, 'cvr': 10.0, 'cpa': 1.0}}
    
    # is_delete=True 일때 조회하지 않음        
    def test_read_when_is_delete_True(self,client,set_user,set_for_result):
        obj=Ad.objects.get(advertiser=37445221)
        obj.is_delete=True
        obj.save()
        response=self.read_result(client,set_user,set_for_result)
        
        assert response.status_code == 404
        assert response.json()      == '존재하지 않는 광고주 id입니다.'

