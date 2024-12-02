from django.urls import path
from .views import Kaizen_view, kaizen_vista
from . import views

urlpatterns = [
    path('Kaizen/', views.Kaizen_view, name='kaizen'),
    path('Kaizen/<int:pk>/', Kaizen_view, name='kaizen'),
    path('actualizar-estado/<int:accion_id>/', views.actualizar_estado, name='actualizar_estado'),
    path('Kaizen/vista/<int:pk>/', kaizen_vista, name='kaizen_vista'), 
]
