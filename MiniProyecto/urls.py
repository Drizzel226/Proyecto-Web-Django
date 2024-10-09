from django.urls import path
from .views import miniproyectos
from . import views

urlpatterns = [
    path('miniproyectos/', views.miniproyectos, name='miniproyectos'),
    
]
