from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.db.models import Q

from base.models import Niveau, Debouche


# Create your views here.
def niveaux(request:HttpRequest):
    get_dict = request.GET
    search=get_dict.get("search","")
    #niveaux = Niveau.objects.filter(lib__icontains=search) #Niveau.objects.filter(lib__contains=search)
    """
    niveaux = Niveau.objects.filter(
        Q(lib__icontains=search) |
        Q(Metier__debouche__lib__icontains=search)
    ) 
    """
    niveaux = Niveau.objects.filter(
        Q(lib__icontains=search)
    )
    nb_niveaux = Niveau.objects.count()
    nb_debouches = Debouche.objects.count()

    """
    niveaux=None
    
    if search:
        niveaux = Niveau.objects.filter(lib=search)
    else:
        niveaux = Niveau.objects.all()  # Niveau.niveaux(Niveau)
    """
    #return HttpResponse(niveaux)
    context={
        "niveaux":niveaux,
        "search":search,
        "nb_debouches":nb_debouches,
        "nb_niveaux":nb_niveaux
    }
    return render(request,"front_office/niveau/niveaux.html",context)

def niveau(request:HttpRequest,id:int):

    niveau = Niveau.objects.get(id=id)
    metiers = niveau.Metier.all()
    ecoles = niveau.Formations.all() #.order_by("lib")
    #return HttpResponse(ecoles)
    context={
        "niveau":niveau,
        "metiers":metiers,
        "ecoles":ecoles
    }
    return render(request,"front_office/niveau/niveau.html",context) 