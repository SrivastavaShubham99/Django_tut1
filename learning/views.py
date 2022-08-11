from django.shortcuts import render
from rest_framework import generics

from .models import RecipeModel
from .serializers import RecipeModelSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RecipeView(generics.CreateAPIView) : 
    serializer_class=RecipeModelSerializer
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class GetRecipeView(generics.ListAPIView) : 
    queryset=RecipeModel.objects.all()
    serializer_class=RecipeModelSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return RecipeModel.objects.filter(created_by=user)

