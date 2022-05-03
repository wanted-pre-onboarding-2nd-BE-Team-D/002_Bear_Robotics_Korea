from django.db import models

from core.models import TimeStampModel


class Result(TimeStampModel):
    restuarants = models.ManyToManyField(
        'restaurants.Menu', through='ResultMenu', related_name='results'
    )
    payment = models.ForeignKey('Payment', on_delete=models.PROTECT)
    numbers_of_party = models.PositiveIntegerField(default=0, null=True, blank=True)
    total_payments = models.DecimalField(
        max_digits=12, decimal_places=2, default=0,
        null=True, blank=True
    )

    class Meta:
        db_table = 'results'


class ResultMenu(TimeStampModel):
    result = models.ForeignKey('Result', on_delete=models.PROTECT)
    menu = models.ForeignKey('restaurants.Menu', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    discount_rate = models.DecimalField(
        max_digits=4, decimal_places=3, default=1,
        null=True, blank=True
    )

    class Meta:
        db_table = 'result_menus'


class Payment(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'payments'
