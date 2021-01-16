from django.shortcuts import render

def index(request, room_name):
    return render(request, 'index.html', { 'room_name': room_name })