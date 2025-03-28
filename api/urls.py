from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cocktails/', views.cocktail_index, name='cocktail-index'),
    path('cocktails/<int:cocktail_id>/', views.cocktail_detail, name='cocktail-detail'),
    path('cocktails/create', views.CocktailCreate.as_view(), name='cocktail-create'),
    path('cocktails/<int:pk>/update/', views.CocktailUpdate.as_view(), name='cocktail-update'),
    path('cocktails/<int:pk>/delete/', views.CocktailDelete.as_view(), name='cocktail-delete')
]
