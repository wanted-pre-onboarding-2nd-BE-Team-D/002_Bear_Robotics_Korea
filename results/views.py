import json

from datetime                   import datetime, timedelta
from django.db.models           import Prefetch, Q, Sum, Count
from django.db.models.functions import TruncYear, TruncMonth, TruncWeek, TruncDay, TruncHour
from rest_framework             import status
from rest_framework.views       import APIView
from rest_framework.response    import Response

from restaurants.models      import Restaurant, Subsidary
from results.models          import Result, ResultMenu


def validation_values(value_01, value_02):
    if value_01 > 0 and value_02 > 0:
        if value_01 < value_02:
            value_01, value_02 = value_02, value_01
    
        return int(value_01), int(value_02)
    
    else:
        raise ValueError(
            {'MESSAGE' : 'VALUES_ERROR','DATA_FORMAT' : 'POSITIVE_INTEGER'},
            status = status.HTTP_400_BAD_REQUEST
        )

def make_query(request):
    start_date = request.query_params.get('start_date', None)
    end_date = request.query_params.get('end_date', None)
    maximum_price = request.query_params.get('maximum_price', None)
    minimum_price = request.query_params.get('minimum_price', None)
    maximum_guest = request.query_params.get('maximum_geust', None)
    minimum_guest = request.query_params.get('minimum_geust', None)
    subsidary = request.query_params.get('subsidary', None)
    
    if start_date and end_date and start_date > end_date:
        return Response(
            {'MESSAGE : START_DATE_CANT_OVER_THAN_END_DATE'}, 
            status=status.HTTP_400_BAD_REQUEST
            )


    datetime_format = '%Y-%m-%d %H:%M:%S'
    start_date = datetime.strptime(start_date, datetime_format)
    end_date = datetime.strptime(end_date, datetime_format) + timedelta(days = 1)

    q = Q(created_at__range = (start_date,end_date))

    if maximum_price and minimum_price:
        maximum_price, minimum_price = validation_values(maximum_price, minimum_price)
        q &= Q(total_payment__range = (minimum_price, maximum_price))

    if maximum_guest and minimum_guest:
        maximum_guest, minimum_guest = validation_values(maximum_guest, minimum_guest)
        q &= Q(number_of_party__range = (minimum_guest, maximum_guest))

    if subsidary:
        q &= Q(subsidary__name = subsidary)

    return Result.objects.filter(q)

def make_result(results, time_window, kpi):
    units = {
        'year' : TruncYear,
        'month' : TruncMonth,
        'week' : TruncWeek,
        'day' : TruncDay,
        'hour' : TruncHour
    }

    if kpi == 'total_payments':
        results = results.annotate(time_unit = units[time_window]('created_at')).values('time_unit')\
        .annotate(value = Sum('total_payments')).\
        values('time_unit', 'value', 'restaurant_id')\
    
    elif kpi == 'payment' or kpi == 'numbers_of_party':
        results = results.annotate(time_unit = units[time_window]('created_at')).values('time_unit')\
        .annotate(value = Count(kpi))\
        .values('time_unit', kpi, 'value', 'restaurant_id')\

    return results


class ResultView(APIView):

    def post(self, request):
        """
        예상 시나리오 : 비비고 서초구 서초동 1호점에서 비비고 만두 1개, 갈비 만두 1개, 비비고 비빔밥 1개 카드로 결제

        data = {
            'restaurant' : '비비고,서초구 서초동,1'(업종, 구역, n호점),
            'menus' : {
                '비비고 만두' : 1,
                '갈비 만두' : 1,
                '비비고 비빔밥' : 1
            },
            'total_payment' : 22500,
            'payment' : 'CARD'
        }
        """
        data = json.loads(request.body)
        restaurant_name = data['restaurant'].split(',')
        name = f'{restaurant_name[0]},{restaurant_name[1]}'
        store = restaurant_name[2]
        menus = data['menus']

        subsidary = Subsidary.objects.prefetch_related(
            Prefetch('restaurant_set', 
                queryset=Restaurant.objects.filter(
                    name = name, 
                    store = store
                ),
                to_attr='get_restaurant'
            ),
            Prefetch('menu_set',
                to_attr='get_menus'
            )
        ).get(name = restaurant_name[0])
        restaurant = subsidary.get_restaurant[0]
        menu_list = {}

        for menu in subsidary.get_menus:
            menu_list[menu.name] = menu
        
        new_result = Result.objects.create(
            subsidary = subsidary,
            restaurant = restaurant,
            numbers_of_party = len(menus),
            total_payments = data['total_payment'],
            payment = data['payment']
        )

        results = [ResultMenu(result = new_result, menu = menu_list[menu], quantity = quantity)
            for menu, quantity in menus.items()
        ]
        
        new_result.resultmenu_set.bulk_create(results)

        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        pass


class SalesKPIView(APIView):

    def get(self, request):
        results = make_query(request)
        time_window = request.query_params.get('time_window', 'day')
        kpi = 'total_payments'

        return Response(make_result(results, time_window, kpi), status = status.HTTP_200_OK)


class PaymentKPIView(APIView):

    def get(self, request):
        results = make_query(request)
        time_window = request.query_params.get('time_window', 'day')
        kpi = 'payment'

        return Response(make_result(results, time_window, kpi), status = status.HTTP_200_OK)


class PartyKPIView(APIView):

    def get(self, request):
        results = make_query(request)
        time_window = request.query_params.get('time_window', 'day')
        kpi = 'numbers_of_party'

        return Response(make_result(results, time_window, kpi), status = status.HTTP_200_OK)