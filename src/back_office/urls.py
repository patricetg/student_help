"""student_help URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from django.http import HttpResponse
from back_office.niveau import views as niveau_v
from back_office.logement import views as logement_v


urlpatterns = [
    path("niveaux/",niveau_v.liste, name="bo_niveaux"),
    path("niveaux/<int:idNiv>",niveau_v.niveau, name="bo_niveau"),
    path("niveaux/create/",niveau_v.create, name="bo_create_niveau"),
    
    path("logements/",logement_v.logements, name="bo_logements"),
    path("logements/create/",logement_v.create, name="bo_create_logement"),
    path("logements/update/<int:id>",logement_v.update, name="bo_update_logement"),
    path("logements/delete/<int:id>",logement_v.delete, name="bo_delete_logement"),
]
