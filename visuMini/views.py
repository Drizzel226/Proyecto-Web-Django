from datetime import date
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from MiniProyecto.models import Miniproyecto
from .models import VisuMiniModel
from visu5.models import Roles

# Función para calcular el porcentaje de "On Time" basado en días transcurridos
def calcula_ot(fecha_inicio):
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

# Función para calcular el porcentaje de UPS basado en el puntaje
def calcular_ups(puntaje_obtenido, puntaje_total):
    if puntaje_total <= 0:  # Evita división por cero o valores no válidos
        return 0
    return round((puntaje_obtenido / puntaje_total) * 100, 2)

# Función para calcular el porcentaje OTIF como el promedio de OT y UPS
def calcular_otif(ot, ups):
    return round((ot + ups) / 2, 2)

# Vista principal para mostrar los datos de "Visualización Mini Proyecto"
def visuMini(request):
    numero_de_preguntas = 12  # Define el número de preguntas para el cálculo de puntaje
    puntaje_maximo_por_pregunta = 5
    puntaje_total = numero_de_preguntas * puntaje_maximo_por_pregunta

    # Obtener el parámetro de búsqueda desde la URL
    query = request.GET.get('q', None)  # Buscar por ID si existe un parámetro 'q'

    if query:
        # Filtrar por ID
        try:
            datos = Miniproyecto.objects.filter(id=query)
        except ValueError:
            datos = Miniproyecto.objects.none()  # Manejar caso donde 'q' no sea un número
    else:
        # Mostrar todos los datos si no hay búsqueda
        datos = Miniproyecto.objects.all().order_by('-id')

    visualizaciones = VisuMiniModel.objects.all()

    for dato in datos:
        visualizacion = visualizaciones.filter(MiniProyecto_id=dato.id).first()
        if visualizacion:
            Estandarizacion_completa = dato.Estandarizacion and dato.Fecha_compromiso3
            Expansion_completa = dato.Expansion and dato.Fecha_compromiso4
            if Estandarizacion_completa or Expansion_completa:
                dato.paso_4 = True
                dato.ot = calcula_ot(dato.fecha_inicio)

                if dato.fecha_inicio and visualizacion.dias is None:
                    hoy = date.today()
                    visualizacion.dias = (hoy - dato.fecha_inicio).days
                    visualizacion.save()
            else:
                dato.paso_4 = False
                dato.ot = 0
                visualizacion.dias = None
                visualizacion.save()

            dato.dias = visualizacion.dias
            puntaje_obtenido = dato.puntaje if dato.puntaje is not None else 0
            dato.ups = calcular_ups(puntaje_obtenido, puntaje_total)
            dato.otif = calcular_otif(dato.ot, dato.ups)
        else:
            dato.paso_4 = False
            dato.ot = 0
            dato.dias = ""
            dato.ups = 0
            dato.otif = 0

    miembro = Roles.objects.filter(email=request.user.email).first()
    es_auditor = (miembro.rol in [2, 4, 6, 7] if miembro else False) or request.user.is_superuser

    paginator = Paginator(datos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    total_pages = paginator.num_pages
    current_page = page_obj.number

    # Generar rango de páginas dinámico
    page_range = []
    if total_pages > 1:
        # Siempre incluir la primera página
        page_range.append(1)

        # Agregar "..." si hay un salto grande entre la primera página y el rango actual
        if current_page > 3:
            page_range.append(None)

        # Agregar las páginas cercanas al número actual
        if current_page - 1 > 1:  # Asegurar que el número anterior no sea 1
            page_range.append(current_page - 1)
        if current_page != 1 and current_page != total_pages:  # Asegurar que no se duplique el primero o último
            page_range.append(current_page)
        if current_page + 1 < total_pages:  # Asegurar que el siguiente número no sea el último
            page_range.append(current_page + 1)

        # Agregar "..." si hay un salto grande entre el rango actual y la última página
        if current_page < total_pages - 2:
            page_range.append(None)

        # Siempre incluir la última página
        page_range.append(total_pages)

    return render(request, "visuMini/visualizacionMini.html", {
        "page_obj": page_obj,
        "page_range": page_range,
        "es_auditor": es_auditor,
        "query": query,
    })

# Vista para actualizar el checkbox mediante AJAX
@csrf_exempt
def actualizar_checkbox(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        MiniProyecto_id = data.get('id')
        estado = data.get('estado')

        try:
            visualizacion = VisuMiniModel.objects.get(MiniProyecto_id=MiniProyecto_id)
            
            # Solo actualizar si paso_4 cambia de False a True por primera vez
            if not visualizacion.paso_4 and estado:
                visualizacion.paso_4 = True
                fecha_inicio = Miniproyecto.objects.get(id=MiniProyecto_id).fecha_inicio

                # Calcular `dias` solo una vez en base a fecha_inicio
                if visualizacion.dias is None:  # Solo calcula si `dias` es None
                    visualizacion.dias = (date.today() - fecha_inicio).days
                visualizacion.porcentaje = calcula_ot(fecha_inicio)
            elif not estado:
                # Resetear `paso_4`, `porcentaje` y `dias` si se desmarca el checkbox
                visualizacion.paso_4 = False
                visualizacion.porcentaje = 0  # Opcional: resetear el porcentaje si se desmarca el checkbox
                visualizacion.dias = None  # Resetear `dias` si `paso_4` es False

            visualizacion.save()
            return JsonResponse({'message': 'Estado del checkbox, porcentaje y días actualizado correctamente'})
        
        except VisuMiniModel.DoesNotExist:
            return JsonResponse({'error': 'Registro no encontrado'}, status=404)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Vista para el dashboard (sin cambios)
def dashboard(request):
    return render(request, 'visuMini/dashboard.html')
