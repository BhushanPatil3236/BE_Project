from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class FoodEstimator(models.Model):
    user            = models.ForeignKey(User,  on_delete=models.CASCADE)
    img             = models.ImageField(verbose_name="Image", upload_to="Food-Images",null=True,blank=True)
    img_name        = models.TextField(verbose_name="Image name",null=True,blank=True)
    sugar           = models.FloatField(verbose_name="sugar",null=True,blank=True)
    fiber           = models.FloatField(verbose_name="fiber",null=True,blank=True)
    serving_size    = models.FloatField(verbose_name="serving_size",null=True,blank=True)
    sodium          = models.FloatField(verbose_name="sodium",null=True,blank=True)
    potassium       = models.FloatField(verbose_name="potassium",null=True,blank=True)
    fat_saturated   = models.FloatField(verbose_name="fat_saturated",null=True,blank=True)
    fat             = models.FloatField(verbose_name="fat",null=True,blank=True)
    calories        = models.FloatField(verbose_name="calories",null=True,blank=True)
    cholesterol     = models.FloatField(verbose_name="cholesterol",null=True,blank=True)
    protein         = models.FloatField(verbose_name="protein",null=True,blank=True)
    carbohydrates   = models.FloatField(verbose_name="carbohydrates",null=True,blank=True)

    def __str__(self):
        return str(f"{self.user} - {self.img_name}")


class RecipeGenerator(models.Model):
    user            = models.ForeignKey(User,  on_delete=models.CASCADE)
    query           = models.TextField(verbose_name="recipe query",null=True,blank=True)
    title           = models.TextField(verbose_name="title",null=True,blank=True)
    ingredients     = models.TextField(verbose_name="ingredients",null=True,blank=True)
    servings        = models.TextField(verbose_name="servings",null=True,blank=True)
    instructions    = models.TextField(verbose_name="instructions",null=True,blank=True)

    def __str__(self):
        return str(f"{self.user} - {self.query}")