from django.contrib import admin
from .models import Topping, Pizza, Subs, Pasta, DinnerPlatter, Salad, SubExtra
# Register your models here.
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(DinnerPlatter)
admin.site.register(Salad)
admin.site.register(SubExtra)
