from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from .forms import LogementForm
from base.models import Logement


# Create your views here.
def create(request:HttpRequest):
    form = LogementForm()

    if request.method=="POST":
        form = LogementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../")
    
    context={
        "form":form
    }
    return render(request,"back_office/logement/create.html",context)


def update(request:HttpRequest,id:int):
    logement=Logement.getById(Logement,id)
    #return HttpResponse(logement)

    form = LogementForm(instance=logement)
    
    if request.method=="POST":
        form = LogementForm(request.POST,instance=logement)
        if form.is_valid():
            form.save()
            return redirect("../")

    context={
        "form":form
    }
    return render(request,"back_office/logement/create.html",context)

def delete(request:HttpRequest,id:int):
    logement = Logement.getById(Logement,id)
    if request.method=="POST":
        logement.delete()
        return redirect("../")

    context = {
        "obj":logement
    }
    return render(request,"back_office/delete.html",context)

def logements(request:HttpRequest):
    #logementModel = Logement()
    logements = Logement.logements(Logement) #logementModel.logements()
    context={
        "logements": logements
    }
    return render(request,"back_office/logement/logements.html",context)

