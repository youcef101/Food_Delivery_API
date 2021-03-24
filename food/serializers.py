from rest_framework import serializers
from .models import Food,Category
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'