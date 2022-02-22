from django.db import models
from django.shortcuts import reverse

# Create your models here.

from ingredient.models import Ingredient


class Recipe(models.Model):

    name = models.CharField(max_length=120)
    ingredients = models.ManyToManyField(Ingredient, related_name="ingredients", blank=True, null=True)
    cooking_time = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pic = models.ImageField(upload_to='recipes', default='no_recipe.jpeg')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
       return reverse ('recipes:recipes_detail', kwargs={'pk': self.pk})

    def get_difficulty(self):
        difficulty = "Unknown"
        cooking_time = self.cooking_time
        ingredients = self.ingredients.all()

        if cooking_time < 10 and len(ingredients) < 4:
            difficulty = "Easy"
        elif cooking_time < 10 and len(ingredients) >= 4:
            difficulty = "Medium"
        elif cooking_time >= 10 and len(ingredients) < 4:
            difficulty = "Intermediate"
        elif cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = "Hard"

        return difficulty
        

# def calculate_difficulty(cooking_time, ingredients):
#     difficulty = "Unknown"
#     if cooking_time < 10 and len(ingredients) < 4:
#         difficulty = "Easy"
#     elif cooking_time < 10 and len(ingredients) >= 4:
#         difficulty = "Medium"
#     elif cooking_time >= 10 and len(ingredients) < 4:
#         difficulty = "Intermediate"
#     elif cooking_time >= 10 and len(ingredients) >= 4:
#         difficulty = "Hard"
#     return difficulty
