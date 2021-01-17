from django.shortcuts import render, redirect
from django_redis import get_redis_connection
import django.contrib.auth

connection = get_redis_connection("default")

def index(request):
    is_in_queue = False

    if request.method == "POST" and request.user.is_authenticated:
        connection.rpush(request.user.Course.code + "-teacher", request.user.id)
        is_in_queue = True

    return render(request, 'index.html')

def queue(request):
    if request.user.is_authenticated:
        data = connection.lpop(request.user.Course.code + "-student").split(":")    
        return redirect("/session/" + data[1])

def authenticate(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)

        if user is not None:
            django.contrib.auth.login(request, user)

        return redirect("/")

    return render(request, "authenticate.html")

def sign_out(request):
    django.contrib.auth.logout(request)

    return redirect("/")

def bye(request):
    return render(request, 'bye.html')

def session(request, token):
    return render(request, 'session.html', { "token": token })