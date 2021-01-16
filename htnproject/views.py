from htnproject.models import Course, School
from django.http import HttpResponse
from django.http.response import HttpResponseServerError
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import random, string

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

def findTutor(request):
    try:
        course = request.POST["course"]
        schoolID = request.POST["schoolid"]

        Course.objects.get(code=course)
        School.objects.get(school_id = schoolID)

        room_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(8))

        return redirect("/room/" + room_id)

    except:
        return redirect("/", {'schoolID_error_message' : "Error: You did not enter a valid school ID."})

def room(request):
    return render('room.html')

def queue(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        return render(request, "queue.html")    