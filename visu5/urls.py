from django.urls import path
from .views import visu, dashboard, editar_porque, eliminar_porque

urlpatterns = [
    path('visu/', visu, name='visu'),
    path('visu/dashboard/', dashboard, name='dashboard'),
]
