import json

from datetime                   import datetime, timedelta
from django.db.models           import Prefetch, Q, F, Sum, Count
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractWeek, ExtractDay, ExtractHour
from rest_framework             import status
from rest_framework.views       import APIView
from rest_framework.response    import Response

from restaurants.models      import Restaurant, Subsidary
from results.models          import Result, ResultMenu

"""
권상현
"""
def validation_values(value_01, value_02):
    """
    쿼리 파라미터로 입력 받은 값의 간단한 검증
    필터링 조건으로 사용할 최소/최대매출, 최소/최대방문객이 0보다 큰 숫자인지 검증하고
    만약 최소/최대치를 반대로 입력할 경우 스왑하여 최소/최대로 변경
    음수를 입력 시 프론트사이드에 ValueError, 에러 메세지, 입력해야 할 데이터 포맷(양수), 400번 코드를 반환
    """
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
    """
    쿼리파라미터로 입력받은 값들을 바탕으로 필터링에 필요한 Q객체 생성
    start_date / end_date --> 프론트 사이드에서 'yyyy-mm-dd HH:MM:SS' 포맷의 문자열 자료형으로 입력받음
    maximum_price / minimum_price --> 프론트 사이드에서 정수 모양의 문자열로 받거나 정수형으로 입력 받음
    maximum_guest / minimum_guest --> maximum_price / minimum_price와 같음
    subsidary --> 어떤 프랜차이즈 매장인지 문자열 자료형으로 입력받음 (ex: '비비고', '빕스버거' 등)
    """
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
        q &= Q(total_price__range = (minimum_price, maximum_price))

    if maximum_guest and minimum_guest:
        maximum_guest, minimum_guest = validation_values(maximum_guest, minimum_guest)
        q &= Q(number_of_party__range = (minimum_guest, maximum_guest))

    if subsidary:
        q &= Q(subsidary__name = subsidary)

    return Result.objects.filter(q)

def make_result(results, time_window, kpi):
    """
    필터링 조건에 따라 만들어진 Q객체로 필터링 한 Result queryset을 바탕으로
    조회하기 원하는 kpi 데이터를 생성해 return 값으로 반환
    """
    units = {
        'year' : ExtractYear('created_at'),
        'month' : ExtractMonth('created_at'),
        'week' : ExtractWeek('created_at'),
        'day' : ExtractDay('created_at'),
        'hour' : ExtractHour('created_at')
    }

    if kpi == 'total_price':
        annotate_option = {
            time_window : units[time_window],
            'values' : Sum(kpi)
        }

        return results.values('restaurant_id').annotate(**annotate_option)

    elif kpi == 'payment' or kpi == 'numbers_of_party':
        annotate_option = {
            time_window : units[time_window],
            'values' : Count(kpi)
        }

        return results.values('restaurant_id', kpi).annotate(**annotate_option)


class ResultView(APIView):

    def get(self, request):
        """
        조회하기 원하는 kpi('total_price', 'numbers_of_party', 'payment'),
        start_date / end_date(필수),
        maximum_price / minimum_price(선택),
        maximum_guest / minimum_guest(선택)),
        subsidary(선택)
        을 쿼리파라미터에 담아 요청 시 해당 조건을 바탕으로 필터링 해 결과 반환
        """
        results = make_query(request)
        time_window = request.query_params.get('time_window', 'day')
        kpi = request.query_params.get('kpi', 'total_price')

        return Response(make_result(results, time_window, kpi), status = status.HTTP_200_OK)

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
            'total_price' : 22500,
            'payment' : 'CARD'
        }

        해당 data 포맷을 바탕으로 요청 시 Result 테이블에 결과 입력, ResultMenu 테이블에 메뉴, 주문 수량 등의 상세 결제정보 입력
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
            total_price = data['total_price'],
            payment = data['payment']
        )

        results = [ResultMenu(result = new_result, menu = menu_list[menu], quantity = quantity)
            for menu, quantity in menus.items()
        ]
        
        new_result.resultmenu_set.bulk_create(results)

        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        """
        주문 취소를 위한 api, 요청 시 is_delete 플래그 작동, True로 변경
        """
        pass