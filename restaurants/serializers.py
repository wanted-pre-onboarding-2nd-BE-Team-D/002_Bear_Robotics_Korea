from rest_framework import serializers
from restaurants.models import Restaurant,Subsidary,Menu,Ward,Neighborhood


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id","created_at","updated_at","delete_at","subsidary","ward")

class SubsidarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsidary
        fields = ["id","created_at","updated_at","name"]

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
        
class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = "__all__"

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = "__all__"
