from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class FoodNutrition(models.Model):
    user                = models.ForeignKey(User,  on_delete=models.CASCADE)
    age                 = models.PositiveSmallIntegerField(verbose_name="Age",)
    diet                = models.BooleanField(verbose_name="Veg/Non-veg", default=True)
    weight              = models.PositiveSmallIntegerField(verbose_name="Weight", null=True, blank=True)
    height              = models.PositiveSmallIntegerField(verbose_name="Height", null=True, blank=True)
    bmi                 = models.FloatField(verbose_name="BMI", null=True, blank=True)
    body_type           = models.TextField(verbose_name="Body Type", null=True, blank=True)
    nutrition_predict   = models.TextField(verbose_name="Diet Prediction", null=True, blank=True)


    def __str__(self):
        return str(f"{self.user} - {self.bmi}")