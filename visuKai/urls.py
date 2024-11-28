# nombre_de_la_app/urls.py
from django.urls import path
from . import views
from .views import visuKai

urlpatterns = [
    path('visu/', views.visuKai, name='visuKai'),
    path('actualizar-checkbox/', views.actualizar_checkbox, name='actualizar_checkbox'),

]
