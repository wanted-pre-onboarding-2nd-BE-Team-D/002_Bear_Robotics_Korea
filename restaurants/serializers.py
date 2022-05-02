from .models     import Subsidary
from rest_framework import serializers

class SubsidarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsidary
        fields = "__all__"
