from django.test import TestCase

# Create your tests here.
from .models import Ingredient 


class IngredientModelTest(TestCase):
    def setUpTestData():
       # Set up non-modified objects used by all test methods
       Ingredient.objects.create(name='Milk')

    def test_ingredient_name(self):
       # Get a book object to test
       i = Ingredient.objects.get(id=1)

       # Get the metadata for the 'name' field and use it to query its data
       field_label = i._meta.get_field('name').verbose_name

       # Compare the value to the expected result
       self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
           # Get a book object to test
           i = Ingredient.objects.get(id=1)

           # Get the metadata for the 'author_name' field and use it to query its max_length
           max_length = i._meta.get_field('name').max_length

           # Compare the value to the expected result i.e. 120
           self.assertEqual(max_length, 120)
