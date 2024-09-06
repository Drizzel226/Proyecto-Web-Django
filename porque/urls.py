# myapp/urls.py

from django.urls import path
from .views import porque_view, paso2_view, paso3_view, paso4_view, paso5_view 

urlpatterns = [
    path('porque/', porque_view, name='porque'),
    path('paso2/', paso2_view, name='paso2'),
    path('paso3/', paso3_view, name='paso3'),
    path('paso4/', paso4_view, name='paso4'),
    path('paso5/', paso5_view, name='paso5'),
        # Nueva ruta para el Paso 2
    
]

