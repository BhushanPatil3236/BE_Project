from rest_framework import serializers
from .models import FoodNutrition


class SetFoodNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodNutrition
        fields = '__all__'

class GetFoodNutritionSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    class Meta:
        model = FoodNutrition
        fields = ["id","user_name","age","diet","weight","height","bmi","body_type","nutrition_predict",]

    def get_user_name(self, obj):
        return obj.user.name