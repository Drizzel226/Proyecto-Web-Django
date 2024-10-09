from django.urls import path
from .views import kaizen
from . import views

urlpatterns = [
    path('kaizen/', views.kaizen, name='kaizen'),
    
]
