from django.http import HttpRequest
from django.shortcuts import render
from django.db.models import Q

from base.models import Metier

# Create your views here.
def metiers(request:HttpRequest):
    get_dict = request.GET
    search=get_dict.get("search","")

    metiers = Metier.objects.filter(
        Q(lib__icontains=search)
    )

    context={
    }
    return render(request,"front_office/metier/metiers.html",context)