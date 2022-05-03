from json

from django.db    import transaction
from django.http  import JsonResponse
from django.utils import timezone
from django.views import View

from results.models      import Result, ResultMenu
from results.serializers import ResultSerializer, ResultMenuSerializer

