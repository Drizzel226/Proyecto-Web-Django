# nombre_de_la_app/urls.py
from django.urls import path
from . import views
from .views import visuMini

urlpatterns = [
    path('visu/', views.visuMini, name='visuMini'),
]
