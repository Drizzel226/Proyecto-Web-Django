from django.urls import path
from .views import Kaizen_view  
from . import views

urlpatterns = [
    path('Kaizen/', views.Kaizen_view, name='kaizen'),  # URL para listar o crear Kaizen, si corresponde
    path('Kaizen/<int:pk>/', Kaizen_view, name='kaizen'),
    path('actualizar-estado/<int:accion_id>/', views.actualizar_estado, name='actualizar_estado'),
]
