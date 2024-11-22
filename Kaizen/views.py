from django.shortcuts import render, redirect, get_object_or_404
from .forms import KaizenForm
from .models import Kaizen, MiembroEquipo, ImagenFuncionamiento, ImagenDeploy, ImagenDescripcion
from django.contrib import messages
from django.utils.timezone import now
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.core.mail import send_mail
from django.http import JsonResponse
from porque.models import Porque
import json

def Kaizen_view(request, pk=None):
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

    # Obtener la instancia de Kaizen si pk es proporcionado
    Kaizen_instance = get_object_or_404(Kaizen, pk=pk) if pk else None

    if request.method == 'POST':
        # Procesar el formulario del Kaizen
        form = KaizenForm(request.POST, request.FILES, instance=Kaizen_instance)

        # Verificar si hay "5 Porqués" para quitar
        porques_a_eliminar = request.POST.get('porques_a_eliminar')
        if porques_a_eliminar:
            porques_ids = porques_a_eliminar.split(',')
            Porque.objects.filter(id__in=porques_ids, Kaizen=Kaizen_instance).update(Kaizen=None)

        if form.is_valid():
            es_nuevo = Kaizen_instance is None
            
            # Guardar la instancia del formulario pero sin guardarla aún en la BD
            Kaizen_instance = form.save(commit=False)

            # Obtener las áreas seleccionadas y almacenarlas como cadena separada por comas
            areas_seleccionadas = form.cleaned_data.get('areas_aplicacion')
            if areas_seleccionadas:
                Kaizen_instance.areas_aplicacion = ','.join(areas_seleccionadas)

            # Asignar la fecha de inicio si es la primera vez que se guarda
            if not Kaizen_instance.fecha_inicio:
                Kaizen_instance.fecha_inicio = now().date()

            # Guardar la instancia en la base de datos
            Kaizen_instance.save()

            # Guardar relaciones ManyToMany (miembros del equipo y responsables)
            form.save_m2m()



            # Guardar las nuevas imágenes subidas en Paso 1
            for image_file in request.FILES.getlist('imagenes_deploy'):
                ImagenDeploy.objects.create(kaizen=Kaizen_instance, imagen=image_file)

            for image_file in request.FILES.getlist('imagenes_descripcion'):
                ImagenDescripcion.objects.create(kaizen=Kaizen_instance, imagen=image_file)

            for image_file in request.FILES.getlist('imagenes_funcionamiento'):
                ImagenFuncionamiento.objects.create(kaizen=Kaizen_instance, imagen=image_file)




            







            # Eliminar imágenes seleccionadas para ser eliminadas en Paso 1
            for image_id in request.POST.get("delete_images_deploy", "").split(","):
                            if image_id:
                                ImagenDeploy.objects.filter(id=image_id).delete()
                        
            for image_id in request.POST.get("delete_images_descripcion", "").split(","):
                            if image_id:
                                ImagenDescripcion.objects.filter(id=image_id).delete()


            for image_id in request.POST.get("delete_images_funcionamiento", "").split(","):
                if image_id:
                    ImagenFuncionamiento.objects.filter(id=image_id).delete()

            

            # Si el formulario es nuevo, enviar el correo
            if es_nuevo:
                emails = [miembro.email for miembro in Kaizen_instance.miembros_equipo.all()]
                nombre = Kaizen_instance.Nombre_Kaizen
                id_analisis = Kaizen_instance.id
                categoria = Kaizen_instance.categoria
                subcategoria = Kaizen_instance.subcategoria
                area = Kaizen_instance.area
                subarea = Kaizen_instance.subarea
                mensaje = f"""
                Has sido asignado a un nuevo proyecto de análisis "Kaizen".

                Detalles:
                - Nombre Kaizen: {nombre}
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
                        'Nuevo "Kaizen" asignado',
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
            return redirect('kaizen', pk=Kaizen_instance.pk)



        else:
            messages.error(request, 'Por favor corrige los errores.')

    else:
        # Si el método es GET (cargar la página por primera vez)
        if Kaizen_instance:
            areas_seleccionadas = Kaizen_instance.areas_aplicacion.split(',') if Kaizen_instance.areas_aplicacion else []
            form = KaizenForm(instance=Kaizen_instance, initial={
                'areas_aplicacion': areas_seleccionadas,
            })
        else:
            form = KaizenForm()

    # Mostrar el paso 1 solo si ya existe la instancia
    mostrar_paso1 = Kaizen_instance is not None

    # Obtener todos los miembros del equipo desde la base de datos
    opciones_miembros = MiembroEquipo.objects.all()

    # Obtener los "5 Porqués" asociados al Kaizen
    porques = Porque.objects.filter(kaizen=Kaizen_instance) if Kaizen_instance else []

    context = {
        'form': form,
        'opciones_area': opciones_area,
        'opciones_subarea': opciones_subarea,
        'opciones_maquina': opciones_maquina,
        'opciones_miembros': opciones_miembros,
        'mostrar_paso1': mostrar_paso1,
        'subcategorias_datos': subcategorias_datos,
        'Kaizen': Kaizen_instance,
        'kaizen_id': Kaizen_instance.id if Kaizen_instance else None,
        'porques': porques,
        'imagenes_funcionamiento': ImagenFuncionamiento.objects.filter(kaizen=Kaizen_instance),
        'imagenes_deploy': ImagenDeploy.objects.filter(kaizen=Kaizen_instance),
        'imagenes_descripcion': ImagenDescripcion.objects.filter(kaizen=Kaizen_instance),
    }

    return render(request, 'Kaizen/kaizen.html', context)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Kaizen

@csrf_exempt
def actualizar_estado(request, accion_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nuevo_estado = data.get("estado", "Pendiente")  # Obtén el estado de la solicitud

            # Obtén la acción por su ID
            accion = Kaizen.objects.get(id=accion_id)
            accion.estado = nuevo_estado  # Actualiza el estado
            accion.save()  # Guarda el cambio en la base de datos

            # Devuelve una respuesta JSON confirmando el éxito
            return JsonResponse({"success": True, "estado": nuevo_estado})
        except Kaizen.DoesNotExist:
            return JsonResponse({"success": False, "error": "Acción no encontrada"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Error de JSON"}, status=400)
    else:
        return JsonResponse({"success": False, "error": "Método no permitido"}, status=405)








