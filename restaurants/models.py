from django.db import models

from core.models import TimeStampModel


class Restaurant(TimeStampModel):
    subsidary = models.ForeignKey('Subsidary', on_delete = models.PROTECT, verbose_name = '프랜차이즈 업종')
    ward      = models.ForeignKey('Ward', on_delete = models.PROTECT, verbose_name = '행정 구역(구) FK')
    name      = models.CharField(max_length = 100, verbose_name = '지점 이름') # ex) '비비고, 서초구 서초동'
    store     = models.PositiveIntegerField(null = True, blank = True, verbose_name = 'n호점')

    class Meta:
        db_table = 'restaurants'


class Subsidary(TimeStampModel):
    name = models.CharField(max_length = 20, verbose_name = '프랜차이즈 이름')

    class Meta:
        db_table = 'subsidaries'


class Menu(TimeStampModel):
    subsidary = models.ForeignKey('Subsidary', on_delete = models.CASCADE, verbose_name = '프랜차이즈 업종')
    name      = models.CharField(max_length = 50, verbose_name = '메뉴 이름')
    price     = models.DecimalField(
        max_digits = 12, decimal_places = 2, null = True, blank = True, verbose_name = '메뉴 가격'
    )

    class Meta:
        db_table = 'menus'


class Ward(models.Model):
    name = models.CharField(max_length = 10, verbose_name = '행정 구역(시,구)')

    class Meta:
        db_table = 'wards'


class Neighborhood(models.Model):
    ward = models.ForeignKey('Ward', on_delete = models.CASCADE, verbose_name = '행정 구역(구) FK')
    name = models.CharField(max_length = 10, verbose_name = '행정구역(동)')

    class Meta:
        db_table = 'neighborhoods'
