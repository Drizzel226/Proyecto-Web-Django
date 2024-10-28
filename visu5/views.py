from datetime import date
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from porque.models import Porque
from .models import Visu5Model, Roles  # Asegúrate de importar el modelo Roles

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
        return 0  # Para días mayores a 10 o negativos

# Vista principal para mostrar los datos de "Visualización 5 Por qué"
def visu(request):
    numero_de_preguntas = 12  # Define aquí el número de preguntas
    puntaje_maximo_por_pregunta = 5  # IMPORTANTE ESTOS DOS PUNTOS 
    puntaje_total = numero_de_preguntas * puntaje_maximo_por_pregunta

    datos = Porque.objects.all().order_by('-id')  # Ordenar de más nuevo a más viejo
    visualizaciones = Visu5Model.objects.all()

    for dato in datos:
        visualizacion = visualizaciones.filter(porque_id=dato.id).first()
        if visualizacion:
            # Condición para marcar 'paso_4' automáticamente
            accion_correctiva_completa = dato.Accion_correctiva and dato.Fecha_compromiso1
            accion_preventiva_completa = dato.Accion_Preventiva and dato.Fecha_compromiso2
            if accion_correctiva_completa or accion_preventiva_completa:
                dato.paso_4 = True
                # Si paso_4 es True, calcular el porcentaje y asignarlo a OT
                dato.ot = f"{calcula_porcentaje(dato.fecha_inicio)}%"
            else:
                dato.paso_4 = False
                dato.ot = ""  # Vacío cuando 'paso_4' es False

            dato.porcentaje = visualizacion.porcentaje
            dato.dias = visualizacion.dias
        else:
            dato.paso_4 = False
            dato.ot = ""
            dato.porcentaje = 0 
            dato.dias = 0  

        # Asegurarnos de que 'dato.puntaje' no sea None antes de la operación
        puntaje_obtenido = dato.puntaje if dato.puntaje is not None else 0
        dato.puntaje = round((puntaje_obtenido / puntaje_total) * 100, 2) if puntaje_total > 0 else 0

        # Calcular el promedio de 'puntaje' y 'porcentaje'
        dato.promedio_puntaje_porcentaje = round((dato.puntaje + dato.porcentaje) / 2, 2)

    # Verificar si el usuario autenticado es un auditor
    miembro = Roles.objects.filter(email=request.user.email).first()
    es_auditor = miembro.rol == 1 if miembro else False  # True si el rol es 1 (auditor)

    # Paginación
    paginator = Paginator(datos, 10)  # Mostrar 10 filas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "visu5/visualizacion5.html", {
        "page_obj": page_obj,
        "es_auditor": es_auditor,  # Pasar la variable al contexto para la plantilla
    })

# Vista para actualizar el checkbox mediante AJAX
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
