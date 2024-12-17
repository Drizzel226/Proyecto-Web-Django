from django.urls import path
from .views import Orr_view, Orr_vista
from . import views

urlpatterns = [
    path('ORR/', views.Orr_view, name='ORR'),
    path('ORR/<int:pk>/', Orr_view, name='ORR'),
    path('actualizar-estado/<int:accion_id>/', views.actualizar_estado, name='actualizar_estado'),
    path('ORR/vista/<int:pk>/', Orr_vista, name='Orr_vista'), 
]
