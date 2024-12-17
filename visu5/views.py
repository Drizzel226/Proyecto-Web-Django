from datetime import date
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from porque.models import Porque
from .models import Visu5Model, Roles  # Asegúrate de importar el modelo Roles

# Función para calcular el porcentaje OT basado en días transcurridos
def calcular_ot(fecha_inicio):
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
    if puntaje_total <= 0:  # Evita división por cero
        return 0
    return round((puntaje_obtenido / puntaje_total) * 100, 2)

# Función para calcular el porcentaje OTIF como el promedio de OT y UPS
def calcular_otif(ot, ups):
    return round((ot + ups) / 2, 2)

# Vista principal para mostrar los datos de "Visualización 5 Por qué"
def visu(request):
    numero_de_preguntas = 11  # Define aquí el número de preguntas
    puntaje_maximo_por_pregunta = 5
    puntaje_total = numero_de_preguntas * puntaje_maximo_por_pregunta

    # Obtener el parámetro de búsqueda desde la URL
    query = request.GET.get('q', None)  # Buscar por ID si existe un parámetro 'q'

    if query:
        # Filtrar por ID
        try:
            datos = Porque.objects.filter(id=query)
        except ValueError:
            datos = Porque.objects.none()  # Manejar caso donde 'q' no sea un número
    else:
        # Mostrar todos los datos si no hay búsqueda
        datos = Porque.objects.all().order_by('-id')

    visualizaciones = Visu5Model.objects.all()

    # Procesar los datos y calcular porcentajes
    for dato in datos:
        visualizacion = visualizaciones.filter(porque_id=dato.id).first()
        if visualizacion:
            # Condición para marcar 'paso_5' automáticamente
            Correctiva_completa = dato.Accion_correctiva and dato.Fecha_compromiso1
            Preventiva_completa = dato.Accion_Preventiva and dato.Fecha_compromiso2
            if Correctiva_completa or Preventiva_completa:
                dato.paso_4 = True
                # Calcular "OT" como porcentaje solo si paso_4 es True
                dato.ot = calcular_ot(dato.fecha_inicio)

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


    for dato in datos:
        visualizacion = visualizaciones.filter(porque_id=dato.id).first()
        if visualizacion:
            # Paso 5: Condición para activar Auditar
            Estandarizacion_completa = dato.Estandarizacion and dato.Fecha_compromiso3
            Expansion_completa = dato.Expansion and dato.Fecha_compromiso4
            if Estandarizacion_completa or Expansion_completa:
                dato.paso_5 = True
                if dato.fecha_inicio and visualizacion.dias is None:
                    hoy = date.today()
                    visualizacion.dias = (hoy - dato.fecha_inicio).days
                    visualizacion.save()
            else:
                dato.paso_5 = False


    miembro = Roles.objects.filter(email=request.user.email).first()
    es_auditor = (miembro.rol in [1, 4, 5, 7] if miembro else False) or request.user.is_superuser

    paginator = Paginator(datos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    total_pages = paginator.num_pages
    current_page = page_obj.number

    # Generar rango dinámico para paginación
    page_range = []
    if total_pages > 1:
        # Siempre incluir la primera página
        page_range.append(1)

        # Agregar "..." si hay un salto grande entre la primera página y el rango actual
        if current_page > 3:
            page_range.append(None)  # Usamos `None` para representar "..."

        # Agregar las páginas cercanas al número actual
        start = max(current_page - 1, 2)  # No menos de la segunda página
        end = min(current_page + 1, total_pages - 1)  # No más de la penúltima página
        page_range.extend(range(start, end + 1))

        # Agregar "..." si hay un salto grande entre el rango actual y la última página
        if current_page < total_pages - 2:
            page_range.append(None)

        # Siempre incluir la última página
        page_range.append(total_pages)

    return render(request, "visu5/visualizacion5.html", {
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
        porque_id = data.get('id')
        estado = data.get('estado')

        try:
            visualizacion = Visu5Model.objects.get(porque_id=porque_id)

            if not visualizacion.paso_4 and estado:
                visualizacion.paso_4 = True
                fecha_inicio = Porque.objects.get(id=porque_id).fecha_inicio

                if visualizacion.dias is None:
                    visualizacion.dias = (date.today() - fecha_inicio).days
                visualizacion.porcentaje = calcular_ot(fecha_inicio)
            elif not estado:
                visualizacion.paso_4 = False
                visualizacion.porcentaje = 0
                visualizacion.dias = None

            visualizacion.save()
            return JsonResponse({'message': 'Estado actualizado correctamente'})

        except Visu5Model.DoesNotExist:
            return JsonResponse({'error': 'Registro no encontrado'}, status=404)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Vista para el dashboard (sin cambios)
def dashboard(request):
    return render(request, 'visu5/dashboard.html')
