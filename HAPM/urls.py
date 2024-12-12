from django.urls import path
from .views import HAPM_vista, HAPM_view
from . import views


urlpatterns = [
    path('HAPM/', views.HAPM_view, name='HAPM'),
    path('HAPM/<int:pk>/', HAPM_view, name='HAPM'),
    path('actualizar-estado/<int:accion_id>/', views.actualizar_estado, name='actualizar_estado'),
    path('HAPM/vista/<int:pk>/', HAPM_vista, name='HAPM_vista'),  
]
