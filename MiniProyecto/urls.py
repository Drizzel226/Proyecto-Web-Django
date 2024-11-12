from django.urls import path
from .views import miniproyecto_view, miniproyecto_vista
from . import views


urlpatterns = [
    path('miniproyectos/', views.miniproyecto_view, name='miniproyectos'),
    path('miniproyectos/<int:pk>/', miniproyecto_view, name='miniproyectos'),
    path('actualizar-estado/<int:accion_id>/', views.actualizar_estado, name='actualizar_estado'),
    path('miniproyectos/vista/<int:pk>/', miniproyecto_vista, name='miniproyecto_vista'),  
]
