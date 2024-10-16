from datetime import date
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from porque.models import Porque
from .models import Visu5Model
from django.core.paginator import Paginator

# Función para calcular el porcentaje con base en la fecha de inicio
def calcula_porcentaje(fecha_inicio):
    hoy = date.today()
    dias_transcurridos = (hoy - fecha_inicio).days

    if dias_transcurridos <= 7:
        return 100
    elif dias_transcurridos == 8:
        return 75
    elif dias_transcurridos == 9:
        return 50
    elif dias_transcurridos == 10:
        return 25
    else:
        return 0  # Para días mayores a 11 o negativos


# Vista principal que muestra los datos en la tabla
def visu(request):
    datos = Porque.objects.all().order_by('-id')  # Ordenar de más nuevo a más viejo
    visualizaciones = Visu5Model.objects.all()

    for dato in datos:
        visualizacion = visualizaciones.filter(porque_id=dato.id).first()
        if visualizacion:
            dato.paso_4 = visualizacion.paso_4
            dato.porcentaje = visualizacion.porcentaje
            dato.dias = visualizacion.dias
        else:
            dato.porcentaje = 0 
            dato.dias = 0  
    # Paginación
    paginator = Paginator(datos, 10)  # Mostrar 10 filas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "visu5/visualizacion5.html", {"page_obj": page_obj})




# Vista para actualizar el checkbox mediante AJAX
from datetime import date

@csrf_exempt
def actualizar_checkbox(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        porque_id = data.get('id')
        estado = data.get('estado')

        try:
            visualizacion = Visu5Model.objects.get(porque_id=porque_id)
            visualizacion.paso_4 = estado

            if estado:
                fecha_inicio = Porque.objects.get(id=porque_id).fecha_inicio
                visualizacion.porcentaje = calcula_porcentaje(fecha_inicio)

                # Calcular la diferencia de días
                hoy = date.today()
                visualizacion.dias = (hoy - fecha_inicio).days
            else:
                visualizacion.dias = 0  # Resetear a 0 si se desmarca el checkbox

            visualizacion.save()
            return JsonResponse({'message': 'Estado del checkbox, porcentaje y días actualizado correctamente'})
        except Visu5Model.DoesNotExist:
            return JsonResponse({'error': 'Registro no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)




# Vista para el dashboard (sin cambios)
def dashboard(request):
    return render(request, 'visu5/dashboard.html')
