from django.test import TestCase
import pytest
from .models import Subsidary
from .views import SubsidaryList,SubsidaryDetail
# Create your tests here.

@pytest.mark.django_db
class SubsidaryTest:
    def createTest(self):
        response = Subsidary.objects.create(name='불닭볶음면 테스터')
        assert response.status_code == 200

    