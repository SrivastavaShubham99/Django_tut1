
from django.urls import path
from .views import RecipeView,GetRecipeView



urlpatterns=[
    path('create/',RecipeView.as_view()),
    path('recipe-list/',GetRecipeView.as_view()),
    path('recipe-list/<int:pk>',GetRecipeView.as_view()),
]