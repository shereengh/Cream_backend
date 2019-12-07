from django.db import models

class Ingredient(models.Model):
	name = models.CharField(max_length=150, unique=True)

	def __str__(self):
		return self.name
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='categories')
    def __str__(self):
    	return self.name

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name',]

class Icecream(models.Model):
	base = models.CharField(max_length=50)
	categories = models.ManyToManyField(Category, related_name='icecream')
	def __str__(self):
		return self.base

class Order(models.Model):
	icecream  = models.ForeignKey(Icecream, on_delete=models.CASCADE, related_name='orders')