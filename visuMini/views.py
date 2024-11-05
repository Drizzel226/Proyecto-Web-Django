from datetime import date
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from MiniProyecto.models import Miniproyecto
from .models import VisuMiniModel, Roles  # Asegúrate de importar el modelo Roles

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
def visuMini(request):
    numero_de_preguntas = 12  # Define aquí el número de preguntas
    puntaje_maximo_por_pregunta = 5
    puntaje_total = numero_de_preguntas * puntaje_maximo_por_pregunta

    datos = Miniproyecto.objects.all().order_by('-id')
    visualizaciones = VisuMiniModel.objects.all()

    for dato in datos:
        visualizacion = visualizaciones.filter(MiniProyecto_id=dato.id).first()
        if visualizacion:
            # Condición para marcar 'paso_4' automáticamente
            accion_correctiva_completa = dato.Accion_correctiva and dato.Fecha_compromiso1
            accion_preventiva_completa = dato.Accion_Preventiva and dato.Fecha_compromiso2
            if accion_correctiva_completa or accion_preventiva_completa:
                dato.paso_4 = True
                # Calcular "OT" como porcentaje y "Días" si paso_4 es True
                dato.ot = f"{calcula_porcentaje(dato.fecha_inicio)}%"
                if dato.fecha_inicio:
                    hoy = date.today()
                    dato.dias = (hoy - dato.fecha_inicio).days
            else:
                dato.paso_4 = False
                dato.ot = ""  # Vacío cuando 'paso_4' es False
                dato.dias = ""  # Vacío cuando 'paso_4' es False

            dato.porcentaje = visualizacion.porcentaje
        else:
            dato.paso_4 = False
            dato.ot = ""
            dato.porcentaje = 0 
            dato.dias = ""  

        puntaje_obtenido = dato.puntaje if dato.puntaje is not None else 0
        dato.puntaje = round((puntaje_obtenido / puntaje_total) * 100, 2) if puntaje_total > 0 else 0
        dato.promedio_puntaje_porcentaje = round((dato.puntaje + dato.porcentaje) / 2, 2)

    # Verificar si el usuario autenticado es un auditor
    miembro = Roles.objects.filter(email=request.user.email).first()
    es_auditor = (miembro.rol == 1 if miembro else False) or request.user.is_superuser

    paginator = Paginator(datos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "visu5/visualizacion5.html", {
        "page_obj": page_obj,
        "es_auditor": es_auditor,
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

                # Calcular solo una vez "dias" en base a fecha_inicio
                visualizacion.dias = (date.today() - fecha_inicio).days  # Guardar los días calculados en la base de datos
                visualizacion.porcentaje = calcula_porcentaje(fecha_inicio)
            elif not estado:
                # Resetear `paso_4` y opcionalmente `porcentaje` si se desmarca el checkbox
                visualizacion.paso_4 = False
                visualizacion.porcentaje = 0  # Opcional: resetear el porcentaje si se desmarca el checkbox
                visualizacion.dias = None  # Dejar en None o resetear si se desmarca `paso_4`

            visualizacion.save()
            return JsonResponse({'message': 'Estado del checkbox, porcentaje y días actualizado correctamente'})
        
        except VisuMiniModel.DoesNotExist:
            return JsonResponse({'error': 'Registro no encontrado'}, status=404)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)


