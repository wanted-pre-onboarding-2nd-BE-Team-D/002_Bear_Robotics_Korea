# Generated by Django 4.0.4 on 2022-05-06 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0008_merge_20220505_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='total_payments',
            new_name='total_price',
        ),
    ]