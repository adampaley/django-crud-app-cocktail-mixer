from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cocktails/', views.cocktail_index, name='cocktail-index'),
    path('cocktails/<int:cocktail_id>/', views.cocktail_detail, name='cocktail-detail'),
    path('cocktails/create', views.CocktailCreate.as_view(), name='cocktail-create'),
    path('cocktails/<int:pk>/update/', views.CocktailUpdate.as_view(), name='cocktail-update'),
    path('cocktails/<int:pk>/delete/', views.CocktailDelete.as_view(), name='cocktail-delete'),
    path('cocktails/<int:cocktail_id>/add-serving/', views.add_serving, name='add-serving'),
    path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredient-create'),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredient-detail'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredient-index'),
    path('ingredients/<int:pk>/update/', views.IngredientUpdate.as_view(), name='ingredient-update'),
    path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredient-delete'),
    path('ingredients/<int:cocktail_id>/associate-ingredient/<int:ingredient_id>', views.associate_ingredient, name="associate-ingredient"),
    path('ingredients/<int:cocktail_id>/remove-ingredient/<int:ingredient_id>', views.remove_ingredient, name="remove-ingredient")
]
