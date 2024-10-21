# porque/urls.py

from django.urls import path
from .views import porque_view, porque_vista

urlpatterns = [
    path('porque/', porque_view, name='porque'),
    path('porque/<int:pk>/', porque_view, name='porque'),
    path('porque/vista/<int:pk>/', porque_vista, name='porque_vista'),
]