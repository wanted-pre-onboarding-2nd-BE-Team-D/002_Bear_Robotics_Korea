# Generated by Django 4.0.4 on 2022-05-06 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_alter_menu_name_alter_menu_price_and_more'),
        ('results', '0009_rename_total_payments_result_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='menus',
            field=models.ManyToManyField(related_name='results', through='results.ResultMenu', to='restaurants.menu', verbose_name='주문 메뉴'),
        ),
        migrations.AlterField(
            model_name='result',
            name='numbers_of_party',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='인원 수'),
        ),
        migrations.AlterField(
            model_name='result',
            name='payment',
            field=models.CharField(max_length=10, verbose_name='결제 수단'),
        ),
        migrations.AlterField(
            model_name='result',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurants.restaurant', verbose_name='매출 발생 매장 FK'),
        ),
        migrations.AlterField(
            model_name='result',
            name='subsidary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurants.subsidary', verbose_name='프랜차이즈 업종'),
        ),
        migrations.AlterField(
            model_name='result',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='주문 총액'),
        ),
        migrations.AlterField(
            model_name='resultmenu',
            name='discount_rate',
            field=models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=4, null=True, verbose_name='할인율'),
        ),
        migrations.AlterField(
            model_name='resultmenu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurants.menu', verbose_name='주문 메뉴'),
        ),
        migrations.AlterField(
            model_name='resultmenu',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='주문 수량'),
        ),
        migrations.AlterField(
            model_name='resultmenu',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='results.result', verbose_name='결제 번호'),
        ),
    ]
