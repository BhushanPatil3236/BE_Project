from rest_framework import serializers
from .models import FoodEstimator,RecipeGenerator


class SetFoodEstimatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodEstimator
        fields = '__all__'

class GetFoodEstimatorSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    class Meta:
        model = FoodEstimator
        fields = ['id','user_name','img','img_name','sugar','fiber','serving_size','sodium','potassium','fat_saturated',
                    'fat','calories','cholesterol','protein','carbohydrates',]
    
    def get_user_name(self, obj):
        return obj.user.name