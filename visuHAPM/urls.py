# nombre_de_la_app/urls.py
from django.urls import path
from . import views
from .views import visuHAPM

urlpatterns = [
    path('visu/', views.visuHAPM, name='visuHAPM'),
    path('actualizar-checkbox/', views.actualizar_checkbox, name='actualizar_checkbox'),

]
