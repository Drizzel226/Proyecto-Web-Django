from django.shortcuts import render

def inicio(request):
    return render(request, 'miapp/inicio.html')

def miniproyectos(request):
    return render(request, 'miapp/miniproyectos.html')

def kaizer(request):
    return render(request, 'miapp/kaizer.html')


def inicio(request):
    context = {}
    if request.user.is_authenticated:
        context['user_name'] = request.user.first_name  # o request.user.username o request.user.get_full_name()
    return render(request, 'miapp/inicio.html', context)

