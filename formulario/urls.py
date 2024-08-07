from django.contrib import admin
from django.urls import path
from formulario.views import formu

urlpatterns = [

    path('',formu),
]
