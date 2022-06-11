from django.contrib import admin
from django.urls import path, include

from mainapp import views

urlpatterns = [

    path('', views.index,name='index'),
    path('dashboard', views.dashboard,name='index'),
]