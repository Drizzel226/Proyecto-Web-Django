from django.shortcuts import render, redirect, get_object_or_404
from .forms import MiniproyectoForm
from .models import Miniproyecto, MiembroEquipo, ImagenMiniproyecto, ImagenFuncionamiento, ImagenAntes, ImagenDespues
from django.contrib import messages
from django.utils.timezone import now
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.core.mail import send_mail
from django.http import JsonResponse
from porque.models import Porque
import json

def miniproyecto_view(request, pk=None):
    # Configuración de Google Sheets API
    SERVICE_ACCOUNT_FILE = r'C:\Users\ccu\Desktop\metodologiaups\json.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SPREADSHEET_ID = '1EQxXtEN6arH3AW_7-3AQ0YVf6Q6HXUNth2y1Oy-oVHM'

    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    def obtener_opciones(rango):
        """Función para obtener las opciones desde Google Sheets."""
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=rango).execute()
        return [opcion[0] for opcion in result.get('values', []) if opcion]

    def obtener_subcategorias_y_datos():
        """Función para obtener las subcategorías y sus datos asociados desde Google Sheets."""
        rango = 'Subcategorias!A2:D'
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=rango).execute()
        valores = result.get('values', [])
        
        subcategorias_datos = []
        for fila in valores:
            if len(fila) >= 4:
                subcategorias_datos.append({
                    'subcategoria': fila[0],
                    'categoria': fila[1],
                    'pilar': fila[2],
                    'kpi_iceo': fila[3]
                })
        return subcategorias_datos

    # Obtener las opciones de Google Sheets
    opciones_area = obtener_opciones('Opciones!A2:A')
    opciones_subarea = obtener_opciones('Opciones!B2:B')
    opciones_maquina = obtener_opciones('Opciones!C2:C')
    
    # Obtener las subcategorías y datos asociados desde la hoja
    subcategorias_datos = obtener_subcategorias_y_datos()

    # Obtener la instancia de Miniproyecto si pk es proporcionado
    miniproyecto_instance = get_object_or_404(Miniproyecto, pk=pk) if pk else None

    if request.method == 'POST':
        # Procesar el formulario del Miniproyecto
        form = MiniproyectoForm(request.POST, request.FILES, instance=miniproyecto_instance)

        # Verificar si hay "5 Porqués" para quitar
        porques_a_eliminar = request.POST.get('porques_a_eliminar')
        if porques_a_eliminar:
            porques_ids = porques_a_eliminar.split(',')
            Porque.objects.filter(id__in=porques_ids, miniproyecto=miniproyecto_instance).update(miniproyecto=None)

        if form.is_valid():
            es_nuevo = miniproyecto_instance is None
            
            # Guardar la instancia del formulario pero sin guardarla aún en la BD
            miniproyecto_instance = form.save(commit=False)

            # Obtener las áreas seleccionadas y almacenarlas como cadena separada por comas
            areas_seleccionadas = form.cleaned_data.get('areas_aplicacion')
            if areas_seleccionadas:
                miniproyecto_instance.areas_aplicacion = ','.join(areas_seleccionadas)

            # Asignar la fecha de inicio si es la primera vez que se guarda
            if not miniproyecto_instance.fecha_inicio:
                miniproyecto_instance.fecha_inicio = now().date()

            # Guardar la instancia en la base de datos
            miniproyecto_instance.save()

            # Guardar relaciones ManyToMany (miembros del equipo y responsables)
            form.save_m2m()



            # Guardar las nuevas imágenes subidas en Paso 1
            for image_file in request.FILES.getlist('imagenes'):
                ImagenMiniproyecto.objects.create(miniproyecto=miniproyecto_instance, imagen=image_file)

            for image_file in request.FILES.getlist('imagenes_funcionamiento'):
                ImagenFuncionamiento.objects.create(miniproyecto=miniproyecto_instance, imagen=image_file)

            for image_file in request.FILES.getlist('imagenes_antes'):
                ImagenAntes.objects.create(miniproyecto=miniproyecto_instance, imagen=image_file)

            for image_file in request.FILES.getlist('imagenes_despues'):
                ImagenDespues.objects.create(miniproyecto=miniproyecto_instance, imagen=image_file)







            # Eliminar imágenes seleccionadas para ser eliminadas en Paso 1
            delete_images = request.POST.get("delete_images", "")
            for image_id in delete_images.split(","):
                if image_id:
                    ImagenMiniproyecto.objects.filter(id=image_id).delete()

            for image_id in request.POST.get("delete_images_funcionamiento", "").split(","):
                if image_id:
                    ImagenFuncionamiento.objects.filter(id=image_id).delete()

            for image_id in request.POST.get("delete_images_antes", "").split(","):
                if image_id:
                    ImagenAntes.objects.filter(id=image_id).delete()

            for image_id in request.POST.get("delete_images_despues", "").split(","):
                if image_id:
                    ImagenDespues.objects.filter(id=image_id).delete()


            # Si el formulario es nuevo, enviar el correo
            if es_nuevo:
                emails = [miembro.email for miembro in miniproyecto_instance.miembros_equipo.all()]
                categoria = miniproyecto_instance.categoria
                id_analisis = miniproyecto_instance.id
                subcategoria = miniproyecto_instance.subcategoria
                area = miniproyecto_instance.area
                subarea = miniproyecto_instance.subarea
                mensaje = f"""
                Has sido asignado a un nuevo proyecto de análisis "Miniproyecto".

                Detalles:
                - ID del Análisis: {id_analisis}
                - Categoría: {categoria}
                - Subcategoría: {subcategoria}
                - Área: {area}
                - Subárea: {subarea}

                Por favor, revisa la plataforma para más detalles.
                """

                # Enviar correo a los miembros del equipo
                try:
                    send_mail(
                        'Nuevo "Miniproyecto" asignado',
                        mensaje,
                        'from@example.com',
                        emails,
                        fail_silently=False,
                    )
                except Exception as e:
                    print(f"Error al enviar el correo: {e}")
                    messages.error(request, f"Error al enviar el correo: {e}")

            # Mensaje de éxito y redirigir con el ID
            messages.success(request, 'Se ha guardado con éxito. Puedes continuar.')
            return redirect('miniproyectos', pk=miniproyecto_instance.pk)

        else:
            messages.error(request, 'Por favor corrige los errores.')

    else:
        # Si el método es GET (cargar la página por primera vez)
        if miniproyecto_instance:
            areas_seleccionadas = miniproyecto_instance.areas_aplicacion.split(',') if miniproyecto_instance.areas_aplicacion else []
            form = MiniproyectoForm(instance=miniproyecto_instance, initial={
                'areas_aplicacion': areas_seleccionadas,
            })
        else:
            form = MiniproyectoForm()

    # Mostrar el paso 1 solo si ya existe la instancia
    mostrar_paso1 = miniproyecto_instance is not None

    # Obtener todos los miembros del equipo desde la base de datos
    opciones_miembros = MiembroEquipo.objects.all()

    # Obtener los "5 Porqués" asociados al Miniproyecto
    porques = Porque.objects.filter(miniproyecto=miniproyecto_instance) if miniproyecto_instance else []

    context = {
        'form': form,
        'opciones_area': opciones_area,
        'opciones_subarea': opciones_subarea,
        'opciones_maquina': opciones_maquina,
        'opciones_miembros': opciones_miembros,
        'mostrar_paso1': mostrar_paso1,
        'subcategorias_datos': subcategorias_datos,
        'miniproyecto': miniproyecto_instance,
        'porques': porques,
        'imagenes_funcionamiento': ImagenFuncionamiento.objects.filter(miniproyecto=miniproyecto_instance),
        'imagenes_antes': ImagenAntes.objects.filter(miniproyecto=miniproyecto_instance),
        'imagenes_despues': ImagenDespues.objects.filter(miniproyecto=miniproyecto_instance),
    }

    return render(request, 'MiniProyecto/miniproyectos.html', context)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Miniproyecto

@csrf_exempt
def actualizar_estado(request, accion_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nuevo_estado = data.get("estado", "Pendiente")  # Obtén el estado de la solicitud

            # Obtén la acción por su ID
            accion = Miniproyecto.objects.get(id=accion_id)
            accion.estado = nuevo_estado  # Actualiza el estado
            accion.save()  # Guarda el cambio en la base de datos

            # Devuelve una respuesta JSON confirmando el éxito
            return JsonResponse({"success": True, "estado": nuevo_estado})
        except Miniproyecto.DoesNotExist:
            return JsonResponse({"success": False, "error": "Acción no encontrada"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Error de JSON"}, status=400)
    else:
        return JsonResponse({"success": False, "error": "Método no permitido"}, status=405)







from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Miniproyecto, ImagenFuncionamiento, ImagenAntes, ImagenDespues
from .forms import MiniproyectoForm
from porque.models import Porque

def miniproyectos_vista(request, pk=None):
    # Obtener la instancia de Miniproyecto
    miniproyecto_instance = get_object_or_404(Miniproyecto, pk=pk) if pk else None

    # Manejo del formulario en método POST
    if request.method == 'POST':
        puntaje_total = request.POST.get('puntaje_total', '0')
        try:
            puntaje_total = int(puntaje_total)
        except ValueError:
            puntaje_total = 0

        if miniproyecto_instance:
            miniproyecto_instance.puntaje = puntaje_total
            miniproyecto_instance.save()
            messages.success(request, f'Formulario guardado exitosamente con el puntaje: {miniproyecto_instance.puntaje}')
            return redirect('miniproyecto_vista', pk=miniproyecto_instance.pk)
        else:
            messages.error(request, 'La instancia no existe.')
    else:
        # Cargar el formulario de Miniproyecto
        form = MiniproyectoForm(instance=miniproyecto_instance)

    # Preparar las preguntas de evaluación
    preguntas = [
        {'paso': 'Paso 0', 'pregunta': ' Se indica el Pilar + Indicador (KPI) / Disparador asociado (KAI)'},
        {'paso': 'PASO 0', 'pregunta': 'Se indica el impacto (pérdida)'},
        {'paso': 'PASO 0', 'pregunta': 'Se especifican los campos mandatorios (fecha, área subárea, integrantes, etc.)'},
        {'paso': 'PASO 1', 'pregunta': 'Se describe correctamente el problema: Qué, Cómo, Cuándo,  Dónde, Quién'},
        {'paso': 'PASO 1', 'pregunta': 'El problema describe correctamente la falla funcional o defecto (lo que es evidente a la vista y que genera la desviación)'},
        {'paso': 'PASO 2', 'pregunta': 'Se describen correctamente los modos de falla / defecto (puntos de partida del análisis 5 PQ)'},
        {'paso': 'PASO 3', 'pregunta': 'Se encuentra definida la causa raíz del problema planteado'},
        {'paso': 'PASO 3', 'pregunta': 'Se ha definido la causa dentro de las 5M (Máquina, Método, Hombre, Materiales, Medio Ambiente)'},
        {'paso': 'PASO 4', 'pregunta': 'Se indican medidas correctivas / Se indican medidas preventivas'},
        {'paso': 'PASO 4', 'pregunta': 'Se indican responsables en cada caso / Se indican fechas de compromiso'},
        {'paso': 'PASO 4', 'pregunta': 'Se cumplen fechas de cierre?'},
        {'paso': 'PASO 5', 'pregunta': '¿Se genera algún nuevo estándar tras este análisis?'},
    ]

    # Configurar opciones de calificación
    ratings = [
        (1, 'Muy insatisfecho'),
        (2, 'Insatisfecho'),
        (3, 'Neutral'),
        (4, 'Satisfecho'),
        (5, 'Muy Satisfecho')
    ]

    # Consultar "5 Porqués" asociados al Miniproyecto
    porques = Porque.objects.filter(miniproyecto=miniproyecto_instance) if miniproyecto_instance else []

    # Obtener imágenes relacionadas para cada sección
    imagenes_funcionamiento = ImagenFuncionamiento.objects.filter(miniproyecto=miniproyecto_instance)
    imagenes_antes = ImagenAntes.objects.filter(miniproyecto=miniproyecto_instance)
    imagenes_despues = ImagenDespues.objects.filter(miniproyecto=miniproyecto_instance)

    # Contexto para el template
    context = {
        'form': form,
        'modo_vista': True,
        'miniproyecto_instance': miniproyecto_instance,
        'preguntas': preguntas,
        'ratings': ratings,
        'porques': porques,
        'imagenes_funcionamiento': imagenes_funcionamiento,
        'imagenes_antes': imagenes_antes,
        'imagenes_despues': imagenes_despues,
        'imagenes': ImagenMiniproyecto.objects.filter(miniproyecto=miniproyecto_instance),

    }

    return render(request, 'MiniProyecto/miniproyectos_vista.html', context)
