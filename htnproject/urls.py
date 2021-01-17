"""htnproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.authenticateUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('findtutor', views.findTutor, name='findtutor'),
    path('queue', views.queue, name='queue'),
    path('room/<str:room_name>', views.room, name='room'),
    path('authenticate', views.authenticate, name='authenticate'),
    path('bye', views.bye, name='bye'),
    path('session', views.session, name='session')
]
