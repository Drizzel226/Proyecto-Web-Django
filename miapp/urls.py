from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('miniproyectos/', views.miniproyectos, name='miniproyectos'),
    path('kaizer/', views.kaizer, name='kaizer'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
]