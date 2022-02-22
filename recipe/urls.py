from django.urls import path
from .views import home, recipes, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
   path('', home),
   path('recipes/', recipes, name='recipes_list'),
   path('recipes/<pk>', RecipeDetailView.as_view(), name='recipes_detail'),
]
