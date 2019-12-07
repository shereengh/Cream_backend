from django.contrib import admin
from .models import Icecream, Order, Category, Ingredient

admin.site.register(Icecream)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Ingredient)
