from django.contrib import admin
from .models import Cocktail, Ingredient, Serving

# Register your models here.
admin.site.register(Cocktail)
admin.site.register(Serving)
admin.site.register(Ingredient)