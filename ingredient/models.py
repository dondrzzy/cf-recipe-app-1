from django.db import models

# Create your models here.


class Ingredient(models.Model):

    name = models.CharField(max_length=120)
    pic = models.ImageField(upload_to='ingredients', default='no_ingredients.jpeg')

    def __str__(self):
        return str(self.name)
