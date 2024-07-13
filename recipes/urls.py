from django.urls import path
from .views import SpoonacularRecipeList, SpoonacularRecipeSearch, create_recipe, delete_recipe

urlpatterns = [
    path('spoonacular/recipes/', SpoonacularRecipeList.as_view(), name='spoonacular-recipes'),
    path('spoonacular/recipes/search/', SpoonacularRecipeSearch.as_view(), name='spoonacular-recipes-search'),
    path('recipes/', create_recipe, name='recipe-create'),
    path('recipes/<int:pk>/', delete_recipe, name='recipe-delete'),
]
