from django.shortcuts import render, redirect
import django.contrib.auth
from django_redis import get_redis_connection
import json

connection = get_redis_connection("default")

def index(request):
    return render(request, 'index.html')

def queue(request):
    if request.user.is_authenticated:
        return redirect("/session/" + connection.lpop(request.user.course.code + "-student").decode("utf-8").split(":")[0])


def authenticate(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)

        if user is not None:
            django.contrib.auth.login(request, user)
        return redirect("/")
    return render(request, "authenticate.html")


def bye(request):
    return render(request, 'bye.html')

def session(request, token):
    return render(request, 'session.html', { "token": token })

def sign_out(request):
    django.contrib.auth.logout(request)

    return redirect("/")