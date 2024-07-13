import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Recipe
from .serializers import RecipeSerializer
from django.conf import settings
from rest_framework.decorators import api_view

class SpoonacularRecipeList(APIView):
    def get(self, request):
        api_key = settings.SPOONACULAR_API_KEY
        url = f'https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&addRecipeInformation=true'
        response = requests.get(url)
        data = response.json()
        return Response(data['results'])

class SpoonacularRecipeSearch(APIView):
    def get(self, request):
        query = request.GET.get('query', '')
        api_key = settings.SPOONACULAR_API_KEY
        url = f'https://api.spoonacular.com/recipes/complexSearch?query={query}&apiKey={api_key}&addRecipeInformation=true'
        response = requests.get(url)
        data = response.json()
        return Response(data['results'])

@api_view(['POST'])
def create_recipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_recipe(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    recipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
