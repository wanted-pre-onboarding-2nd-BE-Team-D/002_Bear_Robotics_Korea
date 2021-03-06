from ast import Sub
import pytest
import json
from django.urls import reverse
from datetime import datetime
from restaurants.models import Subsidary

@pytest.mark.django_db()
class Test_Subsidary:
    """
        류성훈
    """
    
    @pytest.fixture
    def _setup(self, client):
        subsidary = Subsidary.objects.create(name='test')
        return subsidary

    def test_subsidary_get(self, client, _setup):
        # Data detail GET
        response = client.get(
            f'/restaurants/subsidary/{_setup.id}'
        )
        assert response.status_code == 200

    def test_subsidary_list_get(self, client, _setup):
        # Data list GET
        response = client.get(
            '/restaurants/subsidary'
        )
        assert Subsidary.objects.count() == 1
        assert response.status_code == 200

    def test_subsidary_is_delete(self, client, _setup):
        # Post 데이터가 is_delete = False인지
        response = client.get(
            f'/restaurants/subsidary/{_setup.id}'
        )
        assert response.data['is_delete'] == False
        assert response.status_code == 200

    
    def test_subsidary_soft_delete(self, client, _setup):
        # Soft-delete실행하면 is_delete = True로 변경되는지
        temp = {
            "is_delete": True
        }
        
        response = client.put(
            f'/restaurants/subsidary/{_setup.id}',
            json.dumps(temp), content_type = "application/json"
        )
        assert response.data['is_delete'] == True
        assert response.status_code == 200

    def test_subsidary_soft_delete_list(self, client, _setup):
        # Soft-delete된 데이터가 list에 포함되지 않는지
        temp = {
            "is_delete": True
        }

        id = int(_setup.id)

        # 데이터 하나를 Soft-delet한 상태로 넣어둔다.
        soft_delete_data = client.put(
            f'/restaurants/subsidary/{id}',
            json.dumps(temp), content_type = "application/json"
        )
        
        # 데이터 리스트를 조회한다.
        response = client.get(
            '/restaurants/subsidary'
        )
        assert len(response.data) == 0
        assert response.status_code == 200
        

