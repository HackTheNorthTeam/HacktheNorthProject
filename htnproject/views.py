from HacktheNorthProject.htnproject.models import Course
from django.http import HttpResponse
from django.http.response import HttpResponseServerError
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html')

def authenticateUser(request):   
    username = request.POST['username']
    password = request.POST['passwd']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

    return redirect("/")   

def logoutUser(request):
    logout(request)
    return redirect("/")

def joinQueue(request):
    if request.user.is_authenticated:
        course = request.user.course
    else:
        course = request.POST["course"]
        try:
            Course.objects.get(code=course)
        except:
            return redirect("/")