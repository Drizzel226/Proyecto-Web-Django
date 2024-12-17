from datetime import date
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from HAPM.models import Hapm
from .models import VisuHAPMModel
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

# Vista principal para mostrar los datos de "Visualización Hapm"
def visuHAPM(request):
    numero_de_preguntas = 12
    puntaje_maximo_por_pregunta = 5
    puntaje_total = numero_de_preguntas * puntaje_maximo_por_pregunta

    # Obtener y limpiar el parámetro de búsqueda
    query = request.GET.get('q', "").strip()  # Usamos "" como valor predeterminado

    if query:
        try:
            datos = Hapm.objects.filter(id=query)
        except ValueError:
            datos = Hapm.objects.none()  # Si `query` no es un número válido, no devolvemos nada
    else:
        datos = Hapm.objects.all().order_by('-id')

    visualizaciones = VisuHAPMModel.objects.all()

    # Procesar los datos y calcular porcentajes
    for dato in datos:
        visualizacion = visualizaciones.filter(Hapm_id=dato.id).first()
        if visualizacion:
            Correctiva_completa = dato.Accion_correctiva and dato.Fecha_compromiso1
            Preventiva_completa = dato.Accion_Preventiva and dato.Fecha_compromiso2
            if Correctiva_completa or Preventiva_completa:
                dato.paso_4 = True
                dato.ot = calcula_ot(dato.fecha_inicio)

                if dato.fecha_inicio and visualizacion.dias is None:
                    visualizacion.dias = (date.today() - dato.fecha_inicio).days
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
        visualizacion = visualizaciones.filter(Hapm_id=dato.id).first()
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
    es_auditor = (miembro.rol in [2, 4, 6, 7] if miembro else False) or request.user.is_superuser

    paginator = Paginator(datos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    total_pages = paginator.num_pages
    current_page = page_obj.number

    page_range = []
    if total_pages > 1:
        page_range.append(1)
        if current_page > 3:
            page_range.append(None)
        if current_page - 1 > 1:
            page_range.append(current_page - 1)
        if current_page != 1 and current_page != total_pages:
            page_range.append(current_page)
        if current_page + 1 < total_pages:
            page_range.append(current_page + 1)
        if current_page < total_pages - 2:
            page_range.append(None)
        page_range.append(total_pages)

    return render(request, "visuHAPM/visualizacionHAPM.html", {
        "page_obj": page_obj,
        "page_range": page_range,
        "es_auditor": es_auditor,
        "query": query,  # Siempre pasamos la consulta actual para que se mantenga en la paginación
    })

# Vista para actualizar el checkbox mediante AJAX
@csrf_exempt
def actualizar_checkbox(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Hapm_id = data.get('id')
        estado = data.get('estado')

        try:
            visualizacion = VisuHAPMModel.objects.get(Hapm_id=Hapm_id)
            
            # Solo actualizar si paso_4 cambia de False a True por primera vez
            if not visualizacion.paso_4 and estado:
                visualizacion.paso_4 = True
                fecha_inicio = Hapm.objects.get(id=Hapm_id).fecha_inicio

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
        
        except VisuHAPMModel.DoesNotExist:
            return JsonResponse({'error': 'Registro no encontrado'}, status=404)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)
