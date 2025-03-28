from django.contrib import admin
from .models import Cocktail, Serving

# Register your models here.
admin.site.register(Cocktail)
admin.site.register(Serving)