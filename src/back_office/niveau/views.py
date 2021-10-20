from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from base.models import Niveau
from .forms import NiveauForm

# Create your views here.
def create(request:HttpRequest):
    form=NiveauForm()

    if request.method=="POST":
        pass

    context={
        "form":form
    }
    return render(request,"back_office/niveau/create.html",context)

def liste(request:HttpRequest):
    niveaux = Niveau.niveaux(Niveau)
    #return HttpResponse(niveaux)
    context={
        "niveaux":niveaux
    }
    return render(request,"back_office/niveau/niveaux.html",context) 

def niveau(request:HttpRequest,idNiv:int):
    niveau = Niveau.getById(Niveau,idNiv)
    #return HttpResponse(niveau)
    context={
        "niveau":niveau
    }
    return render(request,"back_office/niveau/niveau.html",context) 


