# myapp/urls.py

from django.urls import path
from .views import porque_view, paso2_view

urlpatterns = [
    path('porque/', porque_view, name='porque'),
    path('paso2/', paso2_view, name='paso2'),

        # Nueva ruta para el Paso 2
    
]

