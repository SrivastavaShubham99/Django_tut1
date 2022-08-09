import imp
from django.db import models
# Create your models here.

class RecipeModel(models.Model) : 
    name=models.CharField(max_length=200,null=False)
    date_created=models.DateField(auto_now_add=True)
    created_by=models.CharField(max_length=200,null=True)

