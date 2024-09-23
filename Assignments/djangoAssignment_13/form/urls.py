from django.urls import path
from form import views

urlpatterns = [
    path('', views.user_form_view, name='user_form'),
]
