from rest_framework import serializers

from results.models import Result, ResultMenu


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'created_at', 'updated_at', 'delete_at', 'restaurant',
                  'subsidary', 'menus', 'payment', 'numbers_of_party', 'total_payments']


class ResultMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultMenu
        fields = ['id', 'created_at', 'updated_at', 'delete_at',
                  'result', 'menu', 'quantity', 'discount_rate']
