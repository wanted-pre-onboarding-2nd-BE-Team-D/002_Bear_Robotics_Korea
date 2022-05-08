from django.db import models

from core.models import TimeStampModel


class Result(TimeStampModel):
    restaurant = models.ForeignKey(
        'restaurants.Restaurant', on_delete=models.PROTECT, verbose_name='매출 발생 매장 FK'
    )
    subsidary = models.ForeignKey(
        'restaurants.Subsidary', on_delete=models.PROTECT, verbose_name='프랜차이즈 업종')
    menus = models.ManyToManyField(
        'restaurants.Menu', through='ResultMenu', related_name='results',
        verbose_name='주문 메뉴'
    )
    payment = models.CharField(max_length=10, verbose_name='결제 수단')
    numbers_of_party = models.PositiveIntegerField(null=True, blank=True, verbose_name='인원 수')
    total_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0,
        null=True, blank=True, verbose_name='주문 총액'
    )

    class Meta:
        db_table = 'results'


class ResultMenu(TimeStampModel):
    result = models.ForeignKey('Result', on_delete=models.PROTECT, verbose_name='결제 번호')
    menu = models.ForeignKey('restaurants.Menu', on_delete=models.PROTECT, verbose_name='주문 메뉴')
    quantity = models.PositiveIntegerField(verbose_name='주문 수량')
    discount_rate = models.DecimalField(
        max_digits=4, decimal_places=3, default=1,
        null=True, blank=True, verbose_name='할인율'
    )

    class Meta:
        db_table = 'result_menus'
