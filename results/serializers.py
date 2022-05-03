from rest_framework import serializers

from results.models import Result,ResultMenu,Payment

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


class ResultMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultMenu
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

