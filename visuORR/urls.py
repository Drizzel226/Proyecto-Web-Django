# nombre_de_la_app/urls.py
from django.urls import path
from . import views
from .views import visuORR

urlpatterns = [
    path('visu/', views.visuORR, name='visuORR'),
    path('actualizar-checkbox/', views.actualizar_checkbox, name='actualizar_checkbox'),

]
