import csv
import os
import django
from pprint import pprint

os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')
django.setup()

from results.models import Result


def insert_user_data():
    with open('002_BearRobotics_Data.csv') as data_set:
        data_reader = csv.reader(data_set)
        next(data_reader, None)    

        result_list = []
        
        for row in data_reader:
            result = Result(
                created_at = row[1],
                updated_at = row[1],
                is_delete = 0,
                restaurant_id = row[2],
                subsidary_id = 1,
                total_payments = row[3],
                numbers_of_party = row[4],
                payment = row[5]
            )
            result_list.append(result)

        Result.objects.bulk_create(result_list)

insert_user_data()