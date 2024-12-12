from django.urls import path
from . import views

urlpatterns = [
    path('HAPM/', views.HAPM_view, name='HAPM'),
    path('HAPM/<int:pk>/', views.HAPM_view, name='HAPM'),
]