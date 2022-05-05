# import json
import pytest
import random

# from datetime            import datetime
# from django.test         import TestCase, Client
# from django.urls         import reverse
# from rest_framework      import status
# from rest_framework.test import APITestCase

from restaurants.models  import Restaurant,Subsidary,Menu,Ward,Neighborhood

@pytest.mark.django_db()
class TestViewRestaurant:
    """ 
    김석재
    """
    
    @pytest.fixture
    def _set_db(self, client):
        """ 
        테스트용 db 데이터를 3개씩 입력합니다
        """
        for name in ['맥도날드','버거킹','쉑쉑버거']:            
            Subsidary.objects.create(
                name = f"{name}"
            )
        for name in ['서초구 서초동','관악구 신림동','강남구 개포동']:            
            Ward.objects.create(
                name = f"{name}"
            )
        for ward in Ward.objects.all():            
            Neighborhood.objects.create(
                ward_id = ward.id,
                name    = "서울"
            )
        self.data = {
                    "subsidary" : "맥도날드",
                    "ward"      : "서초구 서초동",
                    "store"     : 1
                     }    
            
    @pytest.fixture
    def _make_db(self, client):
        #테스트용 랜덤 db를 생성합니다
        subsidary_list = [id['id'] for id in Subsidary.objects.values('id')]
        ward_list      = [id['id'] for id in Ward.objects.values('id')]
        
        self.make_count=0
        for _ in range(random.randrange(20,30)):
            ward_id      = random.choice(subsidary_list)
            subsidary_id = random.choice(ward_list)
            store        = random.choice([1,2,3])
            name         = f"{Subsidary.objects.get(id = subsidary_id).name},\
                {Ward.objects.get(id = ward_id).name}점"
            try:
                if Restaurant.objects.get(ward_id = ward_id, subsidary_id = subsidary_id,
                                          store   = store ,  is_delete    = False):
                    pass
            except:
                Restaurant.objects.create(
                ward_id      = ward_id,
                subsidary_id = subsidary_id,
                store        = store,
                name         = name               
                )
                self.make_count += 1
        restaurant_id = [id['id'] for id in Restaurant.objects.values('id')]
        pick_id = random.choice(restaurant_id)
        return pick_id
            
    
    #create
    def test_create_restaurant(self, client, _set_db):
        """         
        POST: resurant
        data:{
                "subsidary" : "맥도날드",
                "ward"      : "서초구 서초동",
                "store"     : 1
            } 
        값을 입력받아 생성           
        status code와 생성된 숫자를 확인
        """
        response = client.post('/restaurants/', data = self.data)
                
        assert response.status_code       == 200
        assert Restaurant.objects.count() == 1
        assert Ward.objects.count()       == 3
        assert Subsidary.objects.count()  == 3
    
    def test_create_restaurant_without_one_data(self, client, _set_db):
        """ 
        POST: resurant
        data:{
                "subsidary" : "맥도날드",
                "ward"      : "서초구 서초동"                
            }
        필수 값이 빠졌을때 생성불가
        status code와 message를 확인
        """        
        del(self.data[f'{random.choice(list(self.data.keys()))}'])        
        response = client.post('/restaurants/', data = self.data)
                
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE' : 'MISSING_VALUE'}
        
    def test_create_restaurant_without_all_data(self, client, _set_db):
        """ 
        POST: resurant
        data:{  
            }
        값이 아예 없을 때 생성불가
        status code와 message를 확인
        """
                
        response = client.post('/restaurants/', data = {})
                
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE' : 'MISSING_VALUE'}
    
    def test_create_restaurant_without_one_value(self, client, _set_db):
        """ 
        POST: resurant
        data:{
                "subsidary" : "",
                "ward"      : "서초구 서초동",
                "store"     : 1
            }
        값이 입력되지 않으면 생성불가
        status code와 message를 확인
        """
        self.data[f'{random.choice(list(self.data.keys()))}'] = ""
        response = client.post('/restaurants/', data = self.data)
                
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE' : 'MISSING_VALUE'}
    
    def test_create_restaurant_duplicate(self, client, _set_db):
        """ 
        POST: resurant
        data:{
                "subsidary" : "맥도날드",
                "ward"      : "서초구 서초동",
                "store"     : 1
            }
        DB에 중복되는 값이 있을땐 생성불가
        status code와 message를 확인
        """
        client.post('/restaurants/', data = self.data)
        response = client.post('/restaurants/', data = self.data)
        
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE': 'DUPLICATE_VALUE'}
    
    
    #read
    def test_read_restaurant_list(self, client, _set_db, _make_db):
        """
        GET: restaurant
        기본 목록 조회  
        status code와 생성된 restaurant 갯수 를 확인
        """
        response = client.get('/restaurants/')
        assert response.status_code       == 200
        assert Restaurant.objects.count() == self.make_count
    
    def test_read_restaurant_search(self, client, _set_db ,_make_db):
        """
        GET: restaurant?search=something
        가게 이름이나 주소로 검색
        status code와 검색된 값의 갯수와 검색된 값중 검색어가 포함되는 갯수를 확인
        """
        subsidary      = [name['name'] for name in Subsidary.objects.values('name')] 
        ward           = [name['name'] for name in Ward.objects.values('name')] 
        token          = subsidary + ward        
        pick_token     = random.choice(token)
        response       = client.get(f'/restaurants/?search={pick_token}')
        search_results = [name['name'] for name in response.json()]
        match_token    = [1 if pick_token in result else 0 for result in search_results]       
        
        assert response.status_code == 200
        assert sum(match_token)     == len(search_results)
    
    def test_read_restaurant_detail(self, client, _set_db, _make_db):    
        """
        GET: restaurant/<id>
        디테일 조회 
        status code와 detail 조회에서 받은 값과 object에서 꺼내온 값이 맞는지 확인
        """
        pick_id    = _make_db           
        response   = client.get(f'/restaurants/{pick_id}')
        obj        = Restaurant.objects.get(id = pick_id)
        
        assert response.status_code     == 200
        assert response.json()['name']  == obj.name
        assert response.json()['store'] == obj.store
        
    def test_read_restaurant_detail_not_exist_value(self, client, _set_db):
        """
        GET: restaurant/<id>
        id에 해당하는 값이 존재하지 않는다면 검색 불가
        status code와 message를 확인
        """
        response   = client.get('/restaurants/1')       
        assert response.status_code == 404
        assert response.json()      == {'MESSAGE' : 'DOES_NOT_EXIST'}
        
    #update
    def test_update_restaurant(self, client, _set_db, _make_db):
        """
        PUT: restaurant/<id>
        data:{
                "subsidary" : "맥도날드",
                "ward"      : "서초구 서초동",
                "store"     : 4
            }
        값을 입력받아 수정
        """
        self.data['store'] = 4
        pick_id            = _make_db        
        obj                = Restaurant.objects.get(id = pick_id)        
        response           = client.put(f'/restaurants/{pick_id}', data = self.data,
                                        content_type = "application/json")
                        
        assert response.status_code       == 200
        assert response.json()['store']   != obj.store
        
    def test_update_restaurant_with_one_data(self, client, _set_db, _make_db):    
        """
        PUT: restaurant/<id>
        data:{
                
                "store"     : 5
                
            }
        한개의 값만 받아도 수정
        """
        self.data['store'] = 5
        pick_id            = _make_db
        obj                = Restaurant.objects.get(id = pick_id)        
        response           = client.put(f'/restaurants/{pick_id}', data = self.data,
                                        content_type = "application/json")
        
        assert response.status_code       == 200
        assert response.json()['store']   != obj.store
    
    def test_update_restaurant_without_all_data(self, client, _set_db, _make_db):  
        """ 
        PUT: restaurant/<id>
        data:{        
            }   
        입력된 값이 없다면 생성불가
        """
        pick_id    = _make_db              
        response   = client.put(f'/restaurants/{pick_id}', data = {},
                                content_type = "application/json")
        
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE' : 'MISSING_VALUE'}
    
    def test_update_restaurant_without_value(self, client, _set_db, _make_db):
        """ 
        PUT: restaurant/<id>
        data:{
                "subsidary" : "",
                "ward"      : "서초구 서초동",
                "store"     : 1
            }
        값이 입력되지 않으면 생성불가
        """
        pick_id    = _make_db  
        self.data[f'{random.choice(list(self.data.keys()))}'] = ""
        response   = client.put(f'/restaurants/{pick_id}', data = self.data,
                                content_type = "application/json")
                
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE' : 'MISSING_VALUE'}
    
    def test_update_restaurant_duplicate(self, client, _set_db, _make_db):
        """ 
        PUT: restaurant/<id>
        data:{
                "subsidary" : "맥도날드",
                "ward"      : "서초구 서초동",
                "store"     : 1
            }
        DB에 중복되는 값이 있을땐 생성불가
        """
        self.data['store'] = 4
        pick_id            = _make_db                        
        client.put(f'/restaurants/{pick_id}', data = self.data,
                   content_type = "application/json")
        response = client.put(f'/restaurants/{pick_id}', data = self.data,
                              content_type = "application/json")                        
        assert response.status_code == 400
        assert response.json()      == {'MESSAGE': 'DUPLICATE_VALUE'}
    
    #delete
    def test_delete_restaurant(self, client, _set_db, _make_db):
        """ 
        DELETE: restaurant/<id>    
        삭제
        """
        pick_id  = _make_db         
        response = client.get(f'/restaurants/{pick_id}')         
        assert response.status_code  == 200
        assert response.json()['id'] == pick_id
        
    def test_delete_restaurant_already_delete(self, client, _set_db, _make_db):
        """ 
        DELETE: restaurant/<id>    
        이미 삭제된 값이면 에러
        """
        pick_id  = _make_db 
        client.delete(f'/restaurants/{pick_id}')
        response = client.get(f'/restaurants/{pick_id}')         
        assert response.status_code == 404
        assert response.json()      == {'MESSAGE': 'DOES_NOT_EXIST'}    
    
    
    
    


