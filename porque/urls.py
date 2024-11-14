# porque/urls.py

from django.urls import path
from .views import porque_view, porque_vista
from .views import asociar_porque_existente, asociar_porque_existentek

urlpatterns = [
    path('porque/', porque_view, name='porque'),
    path('porque/<int:pk>/', porque_view, name='porque'),
    path('porque/vista/<int:pk>/', porque_vista, name='porque_vista'),
    path('asociar_existente/<int:miniproyecto_id>/', asociar_porque_existente, name='asociar_porque_existente'),
    path('asociar_existentek/<int:kaizen_id>/', asociar_porque_existentek, name='asociar_porque_existentek'),
]