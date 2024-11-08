from django.urls import path
from .views import miniproyecto_view
from . import views
from porque.views import asociar_porque_existente

urlpatterns = [
    path('miniproyectos/', views.miniproyecto_view, name='miniproyectos'),
    path('miniproyectos/<int:pk>/', miniproyecto_view, name='miniproyectos'),
    path('actualizar-estado/<int:accion_id>/', views.actualizar_estado, name='actualizar_estado'),
]
