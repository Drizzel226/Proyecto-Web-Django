from django.urls import path
from .views import mi_vista

urlpatterns = [
    path('visu/', mi_vista, name='visuKai'),  # Cambia el nombre aquí
]
