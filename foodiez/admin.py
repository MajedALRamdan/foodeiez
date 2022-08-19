from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Category, Ingredient, Recipe
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe)
