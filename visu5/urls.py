from django.urls import path
from .views import visu, dashboard, editar_porque, eliminar_porque

urlpatterns = [
    path('visu/', visu, name='visu'),
    path('visu/dashboard/', dashboard, name='dashboard'),
    path('visu/editar/<int:pk>/', editar_porque, name='editar_porque'),
    path('visu/eliminar/<int:pk>/', eliminar_porque, name='eliminar_porque'),
]
