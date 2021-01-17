from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def authenticate(request):
    return render(request, 'authenticate.html')

def bye(request):
    return render(request, 'bye.html')

def session(request):
    return render(request, 'session.html')