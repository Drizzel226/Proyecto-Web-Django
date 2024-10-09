from django.urls import path
from .views import visu, dashboard

urlpatterns = [
    path('visu/', visu, name='visu'),
    path('visu/dashboard/', dashboard, name='dashboard'),
]
