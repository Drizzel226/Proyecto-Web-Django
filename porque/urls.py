# myapp/urls.py

from django.urls import path
from .views import porque_view

urlpatterns = [
    path('porque/', porque_view, name='porque'),

    
]

