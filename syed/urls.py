from django.contrib import admin
from django.urls import path
from syed import views

urlpatterns = [
    path('', views.index, name='home'),
    path('view_all', views.view_all, name='view_all'),
]
