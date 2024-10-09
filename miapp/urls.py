from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('no-autorizado/', views.pagina_no_autorizado, name='pagina_no_autorizado'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
]
