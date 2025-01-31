from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json
from rest_framework import status
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import SetFoodEstimatorSerializer,GetFoodEstimatorSerializer
from .models import FoodEstimator
from .predictor import predict_image
import tensorflow.keras.backend as K
from tensorflow.keras.models import load_model

K.clear_session()
path_to_model='model_v1_inceptionV3.h5'
model = load_model(path_to_model)

def get_nutrition(query):
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    response = requests.get(api_url + query, headers={'X-Api-Key': 'ftGj9/D1DTjIAWE8LE2KLw==wWNOM9KStT1ql8QJ'})
    if response.status_code == requests.codes.ok:
        return False, response
    else:
        return True, None

def get_recipe(query):
    api_url = 'https://api.calorieninjas.com/v1/recipe?query='
    response = requests.get(api_url + query, headers={'X-Api-Key': 'ftGj9/D1DTjIAWE8LE2KLw==wWNOM9KStT1ql8QJ'})
    if response.status_code == requests.codes.ok:
        return False, response
    else:
        return True, None

class FoodPridictor(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,format=None):
        try:
            request_data = request.data
            file = request.FILES['image'].file
            query = predict_image(file,model)
            if len(query.strip()) <= 0:
                return Response("this image cannot be able to predict! please try different.", status=status.HTTP_400_BAD_REQUEST)
            is_not_valid,response = get_nutrition(query)
            count=1
            while(is_not_valid):
                if count > 2:
                    return Response("this image cannot be able to predict! please try different.", status=status.HTTP_400_BAD_REQUEST)
                is_not_valid,response = get_nutrition(query)
                count+=1
            if not is_not_valid:
                print(response.text)
                result = json.loads(response.text)
            if len(result['items']) <= 0:
                return Response("this image cannot be able to predict! please try different.", status=status.HTTP_400_BAD_REQUEST)

            request_data['user'] = request.user.pk
            request_data['img_name'] = query
            request_data['sugar'] = result['items'][0]['sugar_g']
            request_data['fiber'] = result['items'][0]['fiber_g']
            request_data['serving_size'] = result['items'][0]['serving_size_g']
            request_data['sodium'] = result['items'][0]['sodium_mg']
            request_data['potassium'] = result['items'][0]['potassium_mg']
            request_data['fat_saturated'] = result['items'][0]['fat_saturated_g']
            request_data['fat'] = result['items'][0]['fat_total_g']
            request_data['calories'] = result['items'][0]['calories']
            request_data['cholesterol'] = result['items'][0]['cholesterol_mg']
            request_data['protein'] = result['items'][0]['protein_g']
            request_data['carbohydrates'] = result['items'][0]['carbohydrates_total_g']
            
            serializer = SetFoodEstimatorSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,format=None):
        try:
            estimator = FoodEstimator.objects.all()
            serializer = GetFoodEstimatorSerializer(estimator, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class RecipeGenerate(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,format=None):
        try:
            request_data = request.data
            query = request_data['query']
            is_not_valid,response = get_recipe(query)
            count=1
            while(is_not_valid):
                if count > 2:
                    return Response("recipe not found!", status=status.HTTP_400_BAD_REQUEST)
                is_not_valid,response = get_recipe(query)
                count+=1
            if not is_not_valid:
                print(response.text)
                result = json.loads(response.text)
            if len(result['items']) <= 0:
                return Response("recipe not found!", status=status.HTTP_400_BAD_REQUEST)
            return Response(result, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)