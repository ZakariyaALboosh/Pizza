from django.db import models
from django.conf import settings
STYLE = (
        ("regular", "Regular") , 
        ("sicilian", "Sicilian")
    )
SIZE = (
        ("small", "Small"),
        ("large", "Large")
    )
toppingsChoices = (
        (0, "No toppings"),
        (1, "One topping"),
        (2, "Two toppings"),
        (3, "Three toppings")
    )    
# Create your models here





class Pasta(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(help_text="Price in U$S",max_digits=4, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} - $ {self.price}"

class Salad(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(help_text="Price in U$S",max_digits=4, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} - $ {self.price}"

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=40)
    size = models.CharField(max_length=10, choices= SIZE)
    price = models.DecimalField(help_text="Price in U$S", max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} - {self.get_size_display()} - $ {self.price}"




class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Pizza(models.Model):


    type = models.CharField(max_length = 10, choices = STYLE)
    size = models.CharField(max_length = 10, choices = SIZE)
    topping = models.IntegerField(choices = toppingsChoices)
    price = models.DecimalField(help_text="Price in U$S", max_digits=5, decimal_places=2)   
    def __str__(self):
        return f"{self.get_type_display()} - {self.get_size_display()} - {self.price} - Toppings: {self.topping}"





class SubExtra(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(help_text="Price in U$S", max_digits=4, decimal_places=2) 

    def __str__(self):
        return f"{self.name} - $ {self.price}"


class Sub(models.Model):
    name = models.CharField(max_length=40)
    size = models.CharField(max_length=10, choices=SIZE)
    price = models.DecimalField(help_text="Price in U$S", max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.get_size_display()} - $ {self.price} "        



class ShoppingCartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )  
    item = models.CharField(max_length=255)
    price = models.DecimalField(help_text="Price in U$S", max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.user} - {self.item} - {self.price}"    