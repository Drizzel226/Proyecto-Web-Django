from django.shortcuts import render

# Create your views here.
# nombre_de_la_app/views.py
from django.http import HttpResponse

def mi_vista(request):
    return render(request, 'visuMini/visualizacionMini.html')
