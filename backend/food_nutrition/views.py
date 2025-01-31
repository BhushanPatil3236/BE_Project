from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json
from rest_framework import status
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import SetFoodNutritionSerializer,GetFoodNutritionSerializer
from .models import FoodNutrition
from .diet_pred import dietFunction


class FoodNutritioner(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,format=None):
        try:
            request_data = request.data
            age = request_data['age']
            diet = request_data['diet']
            weight = request_data['weight']
            height = request_data['height']

            pred = dietFunction(age=age, veg=diet, weight=weight, height=height)

            request_data['user'] = request.user.pk
            request_data['age'] = age
            request_data['diet'] = diet
            request_data['weight'] = weight
            request_data['height'] = height
            request_data['bmi'] = pred[0]
            request_data['body_type'] = pred[1]
            request_data['nutrition_predict'] = ', '.join(pred[2])
            
            serializer = SetFoodNutritionSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,format=None):
        try:
            nutrition = FoodNutrition.objects.all()
            serializer = GetFoodNutritionSerializer(nutrition, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
    