from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages

# Create your views here.
def signin(request:HttpRequest):
    #return HttpResponse("Login  page 4")

    if request.method=="POST":
        post_dic=request.POST
        username = post_dic.get("username",None)
        pwd = post_dic.get("pwd",None)
        user = None
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"Sorry, username or password incorrect !")

        user = authenticate(request,username=username,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request, 'User logged in.')
        else:
            messages.error(request,"Sorry, username or password incorrect !")

    context={}
    return render(request,"authentication/signin.html",context)


def signout(request:HttpRequest):
    logout(request)
    return redirect("fo_home")

def forgotten_pwd(request):
    pass


def register(request:HttpRequest):
    form = UserCreationForm()

    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #create the object, but don't commit to DB
            #user.username = user.username.lower()
            user.save() #commit the object to DB
            login(request, user)
            messages.success(request,"Welcome, your account was successfully created.")
            return redirect("fo_home")
        else:
            messages.error(request,"Error(s) occur(s)")

    context={
        "form":form
    }
    return render(request,"authentication/register.html",context)




