from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def miniproyectos(request):
    return render(request, 'MiniProyecto/miniproyectos.html')