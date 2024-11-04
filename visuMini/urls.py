# nombre_de_la_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('visu/', views.mi_vista, name='visuMini'),
]
