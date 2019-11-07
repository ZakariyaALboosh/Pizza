from django.http import HttpResponse
from django.shortcuts import render
from orders.models import Pasta, Salad, DinnerPlatter, Topping, Pizza, SubExtra, Sub, ShoppingCart
# Create your views here.
def menu_view(request):
    if request.method == "POST" : 
        #take post data and make shopping cart entry with it
        username = request.user
        userShoppingCart = ShoppingCart.objects.filter(user = username)
        if len(userShoppingCart) < 1 :
            pizza_ids = request.POST.getlist('Pizza')
            pizza = Pizza.objects.filter(pk__in= pizza_ids)

            topping_ids = request.POST.getlist('Topping')
            topping = Topping.objects.filter(pk__in= topping_ids)

            salad_ids = request.POST.getlist('Salad')
            salad = Salad.objects.filter(pk__in= salad_ids)

            dinnerplater_ids = request.POST.getlist('DinnerPlatter')
            dinnerplater = DinnerPlatter.objects.filter(pk__in= dinnerplater_ids)

            pasta_ids = request.POST.getlist('Pasta')
            pasta = Pasta.objects.filter(pk__in= pasta_ids)

            subextra_ids = request.POST.getlist('SubExtra')
            subextra = SubExtra.objects.filter(pk__in= subextra_ids)

            sub_ids = request.POST.getlist('Sub')
            sub = Sub.objects.filter(pk__in= sub_ids)



            totalPrice = 0
            items = [pizza , salad , dinnerplater , pasta , subextra , sub]

            for item in items :
                for food in item:
                    totalPrice += food.price


            newCart = ShoppingCart(user = username, price = totalPrice )
            newCart.save()
            itemsdict =  {"Pizza" : pizza , "Salad" :salad , "DinnerPlater" : dinnerplater ,"Pasta" : pasta , "SubExtra" : subextra , "Sub" : sub , "topping" : topping}
            for key , value in itemsdict :
                for food in value : 
                    newCart.key.add(food)
            newCart.save()        
            print(newCart)
        else:
            print(userShoppingCart)    
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
            "Pizza": pizza,
            "Topping": toppings,
            "Salad" : salad,
            "DinnerPlatter" : dinnerPlatter,
            "Pasta" : pasta,
            "SubExtra"  : subExtra,
            "Sub" : sub
          
        }
        return render(request, "orders/menu.html", {'context':context} )