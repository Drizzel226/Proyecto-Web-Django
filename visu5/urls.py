from django.urls import path
from .views import visu, dashboard
from . import views

urlpatterns = [
    path('visu/', visu, name='visu'),
    path('actualizar-checkbox/', views.actualizar_checkbox, name='actualizar_checkbox'),
    path('visu/dashboard/', dashboard, name='dashboard'),
]
