from django.http import HttpResponse
from django.shortcuts import render
from orders.models import Pasta, Salad, DinnerPlatter, Topping, Pizza, SubExtra, Sub
# Create your views here.
def menu_view(request):
    if request.method == "POST" : 
        #take post data and maek shopping cart entry with it.

        


















        print(request.POST)
        return HttpResponse("method is post")


    else:    
        pizza = Pizza.objects.all()
        pasta = Pasta.objects.all()
        salad = Salad.objects.all()
        dinnerPlatter = DinnerPlatter.objects.all()
        toppings = Topping.objects.all()
        subExtra = SubExtra.objects.all()
        sub = Sub.objects.all()
        
        context = {
            "pizza": pizza,
            "toppings": toppings,
            "salad" : salad,
            "dinnerPlatter" : dinnerPlatter,
            "pasta" : pasta,
            "subExtra"  : subExtra,
            "sub" : sub
          
        }
        return render(request, "orders/menu.html", {'context':context} )