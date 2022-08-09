
from rest_framework import serializers
from .models  import RecipeModel


class RecipeModelSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model=RecipeModel
        fields=["name","created_by","date_created"]

    

