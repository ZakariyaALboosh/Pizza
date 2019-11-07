from django.contrib import admin
from .models import Topping, Pizza, Sub, Pasta, DinnerPlatter, Salad, SubExtra, ShoppingCart
# Register your models here.
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(DinnerPlatter)
admin.site.register(Salad)
admin.site.register(SubExtra)
admin.site.register(ShoppingCart)