from django.test import TestCase

# Create your tests here.
from .models import Recipe  # to access Book model
from ingredient.models import Ingredient

class RecipeTestCase(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        i = Ingredient.objects.create(name='milk')
        recipe = Recipe.objects.create(name='Tea', cooking_time=20, description='desc')
        recipe.ingredients.add(i)

    def setUp(self):
        self.recipe = Recipe.objects.get(id=1)

    def test_get_absolute_url(self):
       self.assertEqual(self.recipe.get_absolute_url(), '/recipes/1')

    def test_calc_difficulty(self):
       self.assertEqual(self.recipe.get_difficulty(), 'Intermediate')
