from django.shortcuts import render,redirect
from  .models import Register
from  django.contrib.auth.models import User
from  django.http import  HttpResponse
from django.contrib import messages
from  django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.decorators import login_required


# Create your views here.



def index(request):
    return render(request,"signup.html")


def login(request):
    return  render(request,"login.html")


def home(request):
    return render(request,"home.html")



def registerdata(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password1")
        cpassword=request.POST.get("password2")


        if(password!=cpassword):
            return HttpResponse("Password does not match")
        else:
            user=User.objects.create_user(uname,email,password)
            user.save()
            messages.success(request,"Register Sucessfully")
            return render(request,"signup.html")

@login_required(login_url="login")
def logindata(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("pass")
        user=authenticate(username=username,pass1=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return  HttpResponse("Passowrd and user name does not match")
    return render(request,"login.html")













