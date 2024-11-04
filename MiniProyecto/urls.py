from django.urls import path
from .views import miniproyecto_view
from . import views

urlpatterns = [
    path('miniproyectos/', views.miniproyecto_view, name='miniproyectos'),
    path('miniproyectos/<int:pk>/', miniproyecto_view, name='miniproyectos')

    
]
