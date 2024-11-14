from django.urls import path
from .views import Kaizen_view  
from . import views

urlpatterns = [
    path('Kaizen/', views.Kaizen_view, name='kaizen'),  # URL para listar o crear Kaizen, si corresponde
    path('Kaizen/<int:pk>/', views.Kaizen_view, name='kaizen_detail'),  # URL para detalle de Kaizen por ID
    path('actualizar-estado/<int:accion_id>/', views.actualizar_estado, name='actualizar_estado'),
]
