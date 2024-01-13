from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('404/', page_not_found, name="404"),
    path('contact/', contact, name="contact"),
    path('register/', register, name="register")
]
