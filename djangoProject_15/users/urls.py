from turtle import home

from django.contrib import admin
from django.urls import path, include
from users.views import register, login_view
urlpatterns=[
    path('register/', register),
    path('login/', login_view),
    path('secret-home/', home)
]