from django.db import models

from core.models import TimeStampModel


class Restaurant(TimeStampModel):
    subsidary = models.ForeignKey('Subsidary', on_delete=models.PROTECT)
    ward = models.ForeignKey('Ward', on_delete=models.PROTECT)

    class Meta:
        db_table = 'restaurants'


class Subsidary(TimeStampModel):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'subsidaries'


class Menu(TimeStampModel):
    subsidary = models.ForeignKey('Subsidary', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )

    class Meta:
        db_table = 'menus'


class Ward(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'wards'


class Neighborhood(models.Model):
    ward = models.ForeignKey('Ward', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'neighborhoods'
