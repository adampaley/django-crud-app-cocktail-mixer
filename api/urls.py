from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cocktails/', views.cocktail_index, name='cocktail-index'),
    path('cocktails/<int:cocktail_id>/', views.cocktail_detail, name='cocktail-detail'),
]
