from django.urls import path

from . import views

urlpatterns = [
        path("menu", views.menu_view, name= "menu"),
        path("shoppingcart", views.shoppingCart_view, name = "shoppingcart")

]
