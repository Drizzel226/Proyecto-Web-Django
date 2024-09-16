# myapp/urls.py

from django.urls import path
from .views import porque_view
from . import views

urlpatterns = [
    path('porque/', porque_view, name='porque'),
    path('porque/<int:pk>/', views.porque_view, name='porque'),

    
]

