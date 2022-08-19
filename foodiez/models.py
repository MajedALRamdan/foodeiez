from datetime import timedelta

from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

# Create our models here.
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)
    image = models.ImageField(upload_to="images")
    description = models.TextField(default="")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories"
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(unique=True, max_length=50)
    image = models.ImageField(upload_to="images")
    category_name = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="ingredients",
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    ingredients = models.ManyToManyField(
        Ingredient, related_name="recipes"
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(default="")
    image = models.ImageField(upload_to="images")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recipes"
    )

    def __str__(self):
        return self.name

