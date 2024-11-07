# porque/urls.py

from django.urls import path
from .views import porque_view, porque_vista
from .views import asociar_porque_existente

urlpatterns = [
    path('porque/', porque_view, name='porque'),
    path('porque/<int:pk>/', porque_view, name='porque'),
    path('porque/vista/<int:pk>/', porque_vista, name='porque_vista'),
    path('asociar_existente/<int:miniproyecto_id>/', asociar_porque_existente, name='asociar_porque_existente'),
]