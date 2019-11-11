from django.http import HttpResponse
from django.shortcuts import render, redirect
from orders.models import Pasta, Salad, DinnerPlatter, Topping, Pizza, SubExtra, Sub, ShoppingCart
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def menu_view(request):
    if request.method == "POST" : 
        #take post data and make shopping cart entry with it
        
 
        
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
        if "" in sub_ids :
            sub_ids.remove("")
        sub = Sub.objects.filter(pk__in= sub_ids)



        totalPrice = 0
        items = [pizza , salad , dinnerplater , pasta , subextra , sub]

        for item in items :
            for food in item:
                totalPrice += food.price

        try:
            username = request.user
            userShoppingCart = ShoppingCart.objects.get(user = username)

            itemsdict =  {"pizza" : pizza , "salad" :salad , "dinnerPlater" : dinnerplater ,"pasta" : pasta , "subExtra" : subextra , "sub" : sub , "topping" : topping}

            userShoppingCart.price = totalPrice

            for key , value in itemsdict.items() :
                if key == "pizza" :
                    for food in value :
                        userShoppingCart.pizza.add(food)
                if key == "salad" :
                    for food in value :
                        userShoppingCart.salad.add(food)  
                if key == "dinnerPlater" :
                    for food in value :
                        userShoppingCart.dinnerPlatter.add(food)
                if key == "pasta" :
                    for food in value :
                        userShoppingCart.pasta.add(food)
                if key == "subExtra" :
                    for food in value :
                        userShoppingCart.subExtra.add(food)
                if key == "sub" :
                    for food in value :
                        userShoppingCart.sub.add(food)
                if key == "topping" :
                    for food in value :
                        userShoppingCart.topping.add(food)
                userShoppingCart.save()
        except ObjectDoesNotExist :

            newCart = ShoppingCart(user = username, price = totalPrice )
            newCart.save()

            itemsdict =  {"pizza" : pizza , "salad" :salad , "dinnerPlater" : dinnerplater ,"pasta" : pasta , "subExtra" : subextra , "sub" : sub , "topping" : topping}
           
            for key , value in itemsdict.items() :
                if key == "pizza" :
                    for food in value :
                        newCart.pizza.add(food)
                if key == "salad" :
                    for food in value :
                        newCart.salad.add(food)  
                if key == "dinnerPlater" :
                    for food in value :
                        newCart.dinnerPlatter.add(food)
                if key == "pasta" :
                    for food in value :
                        newCart.pasta.add(food)
                if key == "subExtra" :
                    for food in value :
                        newCart.subExtra.add(food)
                if key == "sub" :
                    for food in value :
                        newCart.sub.add(food)
                if key == "topping" :
                    for food in value :
                        newCart.topping.add(food)                                              
            
            newCart.save()        

        
        print(request.POST)
        return redirect('shoppingcart')

        
 

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


def shoppingCart_view(request):
    if request.method == "GET" :
        pizza = Pizza.objects.all()
        pasta = Pasta.objects.all()
        salad = Salad.objects.all()
        dinnerPlatter = DinnerPlatter.objects.all()
        toppings = Topping.objects.all()
        subExtra = SubExtra.objects.all()
        sub = Sub.objects.all()
        
        username = request.user
        userCart = ShoppingCart.objects.get(user = username)
        upizza = userCart.pizza.all()
        utopping = userCart.topping.all()
        usalad = userCart.salad.all()
        udinnerPlatter = userCart.dinnerPlatter.all()
        upasta = userCart.pasta.all()
        usubExtra = userCart.subExtra.all()
        usub = userCart.sub.all()

        context = {
            "Pizza": pizza,
            "Topping": toppings,
            "Salad" : salad,
            "DinnerPlatter" : dinnerPlatter,
            "Pasta" : pasta,
            "SubExtra"  : subExtra,
            "Sub" : sub
          
        }

        cartitems = {
           "Pizza": upizza,
            "Topping": utopping,
            "Salad" : usalad,
            "DinnerPlatter" : udinnerPlatter,
            "Pasta" : upasta,
            "SubExtra"  : usubExtra,
            "Sub" : usub 
        }

        return render(request, "orders/shoppingCart.html", {'context':context , 'cartitems' : cartitems } )




    else :
         return HttpResponse("method is post")
