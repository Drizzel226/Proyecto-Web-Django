from django.shortcuts import render, redirect, get_object_or_404
from .forms import MiniproyectoForm
from .models import Miniproyecto, MiembroEquipo, ImagenMiniproyecto, ImagenFuncionamiento
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

            # Verificar si el usuario indicó eliminar la imagen de falla funcional (Paso 1)
            if request.POST.get('delete_image') == 'true' and miniproyecto_instance.imagen_falla_funcional:
                miniproyecto_instance.imagen_falla_funcional.delete(save=False)
                miniproyecto_instance.imagen_falla_funcional = None

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

            # Guardar las nuevas imágenes subidas en Paso 2 (Funcionamiento)
            for image_file in request.FILES.getlist('imagen_funcionamiento_files'):
                ImagenFuncionamiento.objects.create(miniproyecto=miniproyecto_instance, imagen=image_file)

            # Eliminar imágenes seleccionadas para ser eliminadas en Paso 1
            delete_images = request.POST.get("delete_images", "")
            for image_id in delete_images.split(","):
                if image_id:
                    ImagenMiniproyecto.objects.filter(id=image_id).delete()

            # Eliminar imágenes seleccionadas para ser eliminadas en Paso 2
            delete_funcionamiento_images = request.POST.get("delete_funcionamiento_images", "")
            for image_id in delete_funcionamiento_images.split(","):
                if image_id:
                    ImagenFuncionamiento.objects.filter(id=image_id).delete()

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

    # Obtener imágenes existentes para mostrar en la plantilla
    imagenes_paso1 = ImagenMiniproyecto.objects.filter(miniproyecto=miniproyecto_instance) if miniproyecto_instance else []
    imagenes_paso2 = ImagenFuncionamiento.objects.filter(miniproyecto=miniproyecto_instance) if miniproyecto_instance else []

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
        'imagenes_paso1': imagenes_paso1,
        'imagenes_paso2': imagenes_paso2,
        'porques': porques,
    }

    return render(request, 'MiniProyecto/miniproyectos.html', context)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def actualizar_estado(request):
    if request.method == "POST":
        data = json.loads(request.body)
        miniproyecto_id = data.get("miniproyecto_id")
        nuevo_estado = data.get("nuevo_estado")

        try:
            miniproyecto = Miniproyecto.objects.get(id=miniproyecto_id)
            miniproyecto.estado = nuevo_estado  # Actualizar el estado en la base de datos
            miniproyecto.save()
            return JsonResponse({"success": True})
        except Miniproyecto.DoesNotExist:
            return JsonResponse({"success": False, "error": "Miniproyecto no encontrado."})
    return JsonResponse({"success": False, "error": "Método no permitido."})
