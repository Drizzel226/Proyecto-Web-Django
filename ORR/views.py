from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrrForm
from .models import Orr, MiembroEquipo, ImagenDeploy, ImagenDescripcion, ImagenDefinir, ImagenEstandar, ImagenExpansion
from django.contrib import messages
from django.utils.timezone import now
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.core.mail import send_mail
from django.http import JsonResponse
from porque.models import Porque
import json

def Orr_view(request, pk=None):
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

    # Obtener la instancia de Orr si pk es proporcionado
    orr_instance = get_object_or_404(Orr, pk=pk) if pk else None
    

    # Obtener la instancia de Orr si pk es proporcionado
    orr_instance = get_object_or_404(Orr, pk=pk) if pk else None

    # Verifica que orr_instance no sea None antes de acceder a su ID
    if orr_instance:
        porques = Porque.objects.filter(orr_id=orr_instance.id)
        imagenes_deploy = ImagenDeploy.objects.filter(orr_id=orr_instance.id)
        imagenes_descripcion = ImagenDescripcion.objects.filter(orr_id=orr_instance.id)
        imagenes_definir = ImagenDefinir.objects.filter(orr_id=orr_instance.id)
        imagenes_estandar = ImagenEstandar.objects.filter(orr_id=orr_instance.id)
        imagenes_expansion = ImagenExpansion.objects.filter(orr_id=orr_instance.id)
    else:
        porques = []
        imagenes_deploy = []
        imagenes_descripcion = []
        imagenes_definir = []
        imagenes_estandar = []
        imagenes_expansion = []


    if request.method == 'POST':
        # Procesar el formulario del Orr
        form = OrrForm(request.POST, request.FILES, instance=orr_instance)

        # Verificar si hay "5 Porqués" para quitar
        porques_a_eliminar = request.POST.get('porques_a_eliminar')
        if porques_a_eliminar:
            porques_ids = porques_a_eliminar.split(',')
            Porque.objects.filter(id__in=porques_ids, orr=orr_instance).update(orr=None)


        if form.is_valid():
            es_nuevo = orr_instance is None
            
            # Guardar la instancia del formulario pero sin guardarla aún en la BD
            orr_instance = form.save(commit=False)

            # Obtener las áreas seleccionadas y almacenarlas como cadena separada por comas
            areas_seleccionadas = form.cleaned_data.get('areas_aplicacion')
            if areas_seleccionadas:
                orr_instance.areas_aplicacion = ','.join(areas_seleccionadas)

            # Asignar la fecha de inicio si es la primera vez que se guarda
            if not orr_instance.fecha_inicio:
                orr_instance.fecha_inicio = now().date()

            # Guardar la instancia en la base de datos
            orr_instance.save()

            # Guardar relaciones ManyToMany (miembros del equipo y responsables)
            form.save_m2m()



            # Guardar las nuevas imágenes subidas en Paso 1
            for image_file in request.FILES.getlist('imagenes_deploy'):
                ImagenDeploy.objects.create(orr=orr_instance, imagen=image_file)

            for image_file in request.FILES.getlist('imagenes_descripcion'):
                ImagenDescripcion.objects.create(orr=orr_instance, imagen=image_file)

            for image_file in request.FILES.getlist('imagenes_definir'):
                ImagenDefinir.objects.create(orr=orr_instance, imagen=image_file)

            for image_file in request.FILES.getlist('imagenes_estandar'):
                ImagenEstandar.objects.create(orr=orr_instance, imagen=image_file)
            
            for image_file in request.FILES.getlist('imagenes_expansion'):
                ImagenExpansion.objects.create(orr=orr_instance, imagen=image_file)
            







            # Eliminar imágenes seleccionadas para ser eliminadas en Paso 1
            for image_id in request.POST.get("delete_images_deploy", "").split(","):
                            if image_id:
                                ImagenDeploy.objects.filter(id=image_id).delete()
                        
            for image_id in request.POST.get("delete_images_descripcion", "").split(","):
                            if image_id:
                                ImagenDescripcion.objects.filter(id=image_id).delete()

            for image_id in request.POST.get("delete_images_definir", "").split(","):
                            if image_id:
                                ImagenDefinir.objects.filter(id=image_id).delete()
                    
            for image_id in request.POST.get("delete_images_estandar", "").split(","):
                            if image_id:
                                ImagenEstandar.objects.filter(id=image_id).delete()
            
            for image_id in request.POST.get("delete_images_expansion", "").split(","):
                            if image_id:
                                ImagenExpansion.objects.filter(id=image_id).delete()
            
            

            # Si el formulario es nuevo, enviar el correo
            if es_nuevo:
                emails = [miembro.email for miembro in orr_instance.miembros_equipo.all()]
                nombre = orr_instance.Nombre_ORR
                id_analisis = orr_instance.id
                categoria = orr_instance.categoria
                subcategoria = orr_instance.subcategoria
                area = orr_instance.area
                subarea = orr_instance.subarea
                mensaje = f"""
                Has sido asignado a un nuevo proyecto de análisis "Orr".

                Detalles:
                - Nombre Orr: {nombre}
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
                        'Nuevo "Orr" asignado',
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
            return redirect('ORR', pk=orr_instance.pk)



        else:
            messages.error(request, 'Por favor corrige los errores.')

    else:
        # Si el método es GET (cargar la página por primera vez)
        if orr_instance:
            areas_seleccionadas = orr_instance.areas_aplicacion.split(',') if orr_instance.areas_aplicacion else []
            form = OrrForm(instance=orr_instance, initial={
                'areas_aplicacion': areas_seleccionadas,
            })
        else:
            form = OrrForm()

    # Mostrar el paso 1 solo si ya existe la instancia
    mostrar_paso1 = orr_instance is not None

    # Obtener todos los miembros del equipo desde la base de datos
    opciones_miembros = MiembroEquipo.objects.all()

    # Obtener los "5 Porqués" asociados al Orr
    porques = Porque.objects.filter(orr_id=orr_instance.id) if orr_instance else []

    context = {
        'form': form,
        'opciones_area': opciones_area,
        'opciones_subarea': opciones_subarea,
        'opciones_maquina': opciones_maquina,
        'opciones_miembros': opciones_miembros,
        'mostrar_paso1': mostrar_paso1,
        'subcategorias_datos': subcategorias_datos,
        'Orr': orr_instance,
        'orr_id': orr_instance.id if orr_instance else None,
        'porques': porques,
        'imagenes_deploy': imagenes_deploy,
        'imagenes_descripcion': imagenes_descripcion,
        'imagenes_definir': imagenes_definir,
        'imagenes_estandar': imagenes_estandar,
        'imagenes_expansion': imagenes_expansion,
    }


    return render(request, 'ORR/ORR.html', context)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Orr

@csrf_exempt
def actualizar_estado(request, accion_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nuevo_estado = data.get("estado", "Pendiente")  # Obtén el estado de la solicitud

            # Obtén la acción por su ID
            accion = Orr.objects.get(id=accion_id)
            accion.estado = nuevo_estado  # Actualiza el estado
            accion.save()  # Guarda el cambio en la base de datos

            # Devuelve una respuesta JSON confirmando el éxito
            return JsonResponse({"success": True, "estado": nuevo_estado})
        except Orr.DoesNotExist:
            return JsonResponse({"success": False, "error": "Acción no encontrada"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Error de JSON"}, status=400)
    else:
        return JsonResponse({"success": False, "error": "Método no permitido"}, status=405)



from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Orr
from .forms import OrrForm

def Orr_vista(request, pk=None):
    # Obtener la instancia de Orr, si existe
    orr_instance = get_object_or_404(Orr, pk=pk) if pk else None

    if request.method == 'POST':
        # Procesar el puntaje total enviado
        puntaje_total = request.POST.get('puntaje_total', '0')
        try:
            puntaje_total = int(puntaje_total)
        except ValueError:
            puntaje_total = 0

        if orr_instance:
            # Guardar el puntaje en la instancia de Orr
            orr_instance.puntaje = puntaje_total
            orr_instance.save()
            messages.success(request, f'Formulario guardado exitosamente con el puntaje: {orr_instance.puntaje}')
            return redirect('Orr_vista', pk=orr_instance.pk)
        else:
            messages.error(request, 'La instancia no existe.')
    else:
        # Si el método es GET, cargar el formulario con la instancia de Orr
        form = OrrForm(instance=orr_instance)

    # Preparar las preguntas de evaluación
    preguntas = [
        {'paso': 'Paso 0', 'pregunta': 'Se indica el Pilar + Indicador (KPI) / Disparador asociado (KAI)'},
        {'paso': 'Paso 0', 'pregunta': 'Se indica el impacto (pérdida)'},
        {'paso': 'Paso 0', 'pregunta': 'Se especifican los campos mandatorios (fecha, área subárea, integrantes, etc.)'},
        {'paso': 'Paso 1', 'pregunta': 'Se describe correctamente el problema: Qué, Cómo, Cuándo, Dónde, Quién'},
        {'paso': 'Paso 1', 'pregunta': 'El problema describe correctamente la falla funcional o defecto (lo que es evidente a la vista y que genera la desviación)'},
        {'paso': 'Paso 2', 'pregunta': 'Se describen correctamente los modos de falla / defecto (puntos de partida del análisis 5 PQ)'},
        {'paso': 'Paso 3', 'pregunta': 'Se encuentra definida la causa raíz del problema planteado'},
        {'paso': 'Paso 3', 'pregunta': 'Se ha definido la causa dentro de las 5M (Máquina, Método, Hombre, Materiales, Medio Ambiente)'},
        {'paso': 'Paso 4', 'pregunta': 'Se indican medidas correctivas / Se indican medidas preventivas'},
        {'paso': 'Paso 4', 'pregunta': 'Se indican responsables en cada caso / Se indican fechas de compromiso'},
        {'paso': 'Paso 4', 'pregunta': 'Se cumplen fechas de cierre?'},
        {'paso': 'Paso 5', 'pregunta': '¿Se genera algún nuevo estándar tras este análisis?'},
    ]

    # Opciones de calificación
    ratings = [
        (1, 'Muy insatisfecho'),
        (2, 'Insatisfecho'),
        (3, 'Neutral'),
        (4, 'Satisfecho'),
        (5, 'Muy Satisfecho')
    ]

    # Consultar "5 Porqués" asociados al Orr
    porques = Porque.objects.filter(orr_id=orr_instance.id) if orr_instance else []

    # Obtener imágenes relacionadas para cada sección
    imagenes_deploy = ImagenDeploy.objects.filter(orr_id=orr_instance.id)
    imagenes_descripcion = ImagenDescripcion.objects.filter(orr_id=orr_instance.id)
    imagenes_definir = ImagenDefinir.objects.filter(orr_id=orr_instance.id)
    imagenes_estandar = ImagenEstandar.objects.filter(orr_id=orr_instance.id)
    imagenes_expansion = ImagenExpansion.objects.filter(orr_id=orr_instance.id)
   

    # Contexto para el template
    context = {
        'form': form,
        'modo_vista': True,
        'orr_instance': orr_instance,
        'preguntas': preguntas,
        'ratings': ratings,
        'porques': porques,
        'imagenes_deploy': imagenes_deploy,
        'imagenes_descripcion': imagenes_descripcion,
        'imagenes_definir': imagenes_definir,
        'imagenes_estandar': imagenes_estandar,
        'imagenes_expansion': imagenes_expansion,
       
        
    }

    return render(request, 'ORR/ORR_vista.html', context)





