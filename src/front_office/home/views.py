from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.
def home(request:HttpRequest):
    #return HttpResponse("home page 2")
    return render(request,"front_office/home/home.html")
