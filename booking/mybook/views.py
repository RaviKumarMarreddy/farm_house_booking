
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html',{})


def signin(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return  redirect("/")
        else:
            return HttpResponse("No user found with given credentials")
    return render (request, 'signin.html',{})

def signup(request):
    if request.method=="POST":

        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name =request.POST['last_name']
        email=request.POST['email']
        new_user= User.objects.create_user(
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            email = email
        )
        new_user.save()
        return  redirect("/signin/")
    form= SignupForm()
    return render(request, 'signup.html', {'form': form})


def signout(request):
    logout(request)
    return render (request, 'index.html',{})

def restro(request):
    return render(request, 'restro.html', {})

def tents(request):
    return render(request, 'tents.html', {})

# def addtentsdetails(request):
#     if request.method=="POST":
#         new_blog=Blog.objects.create(
#             title=request.POST['title'],
#             description=request.POST['description'])
#         new_blog.save()
#         return redirect("/")
#     return render (request, 'addblog.html',{})