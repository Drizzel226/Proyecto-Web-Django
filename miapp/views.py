from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def inicio(request):
    # Permitir que todos vean el menú principal
    return render(request, 'miapp/inicio.html')

@login_required
def miniproyectos(request):
    return render(request, 'miapp/miniproyectos.html')

@login_required
def kaizer(request):
    return render(request, 'miapp/kaizer.html')

def pagina_no_autorizado(request):
    return render(request, 'miapp/no_autorizado.html')
