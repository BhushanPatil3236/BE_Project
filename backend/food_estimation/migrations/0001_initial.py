# Generated by Django 4.1.5 on 2024-01-28 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeGenerator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField(blank=True, null=True, verbose_name='recipe query')),
                ('title', models.TextField(blank=True, null=True, verbose_name='title')),
                ('ingredients', models.TextField(blank=True, null=True, verbose_name='ingredients')),
                ('servings', models.TextField(blank=True, null=True, verbose_name='servings')),
                ('instructions', models.TextField(blank=True, null=True, verbose_name='instructions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FoodEstimator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='Food-Images', verbose_name='Image')),
                ('img_name', models.TextField(blank=True, null=True, verbose_name='Image name')),
                ('sugar', models.FloatField(blank=True, null=True, verbose_name='sugar')),
                ('fiber', models.FloatField(blank=True, null=True, verbose_name='fiber')),
                ('serving_size', models.FloatField(blank=True, null=True, verbose_name='serving_size')),
                ('sodium', models.FloatField(blank=True, null=True, verbose_name='sodium')),
                ('potassium', models.FloatField(blank=True, null=True, verbose_name='potassium')),
                ('fat_saturated', models.FloatField(blank=True, null=True, verbose_name='fat_saturated')),
                ('fat', models.FloatField(blank=True, null=True, verbose_name='fat')),
                ('calories', models.FloatField(blank=True, null=True, verbose_name='calories')),
                ('cholesterol', models.FloatField(blank=True, null=True, verbose_name='cholesterol')),
                ('protein', models.FloatField(blank=True, null=True, verbose_name='protein')),
                ('carbohydrates', models.FloatField(blank=True, null=True, verbose_name='carbohydrates')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
