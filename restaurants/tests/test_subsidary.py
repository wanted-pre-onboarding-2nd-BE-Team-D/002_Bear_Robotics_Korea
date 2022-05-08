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