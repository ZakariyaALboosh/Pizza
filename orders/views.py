from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def menu_view(request):
    
    return HttpResponse("good!")