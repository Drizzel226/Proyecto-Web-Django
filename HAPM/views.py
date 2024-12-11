from django.shortcuts import render, redirect, get_object_or_404
from .forms import HapmForm
from .models import Hapm, MiembroEquipo, ImagenFallaFun, ImagenFalla, ImagenFuncionamiento
from django.contrib import messages
from django.utils.timezone import now
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.core.mail import send_mail  # Importar para enviar correos

def HAPM_view(request, pk=None):
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
        rango = 'Subcategorias!A2:D'  # Asegúrate de que el rango sea correcto en Google Sheets
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=rango).execute()
        valores = result.get('values', [])
        
        # Crear una lista de diccionarios para almacenar los datos
        subcategorias_datos = []
        for fila in valores:
            if len(fila) >= 4:  # Asegúrate de que la fila tenga al menos 4 columnas
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
   # print(subcategorias_datos)

    # Obtener la instancia de Hapm si pk es proporcionado
    hapm_instance = get_object_or_404(Hapm, pk=pk) if pk else None

    if request.method == 'POST':
        form = HapmForm(request.POST, request.FILES, instance=hapm_instance)

        if form.is_valid():
            # Verificar si es un nuevo formulario (no tiene PK aún)
            es_nuevo = hapm_instance is None
            
            # Guardar la instancia del formulario pero sin guardarla aún en la BD
            hapm_instance = form.save(commit=False)

            # Obtener las áreas seleccionadas y almacenarlas como cadena separada por comas
            areas_seleccionadas = form.cleaned_data.get('areas_aplicacion')
            if areas_seleccionadas:
                hapm_instance.areas_aplicacion = ','.join(areas_seleccionadas)

            # Asignar la fecha de inicio si es la primera vez que se guarda
            if not hapm_instance.fecha_inicio:
                hapm_instance.fecha_inicio = now().date()

            # Manejo explícito de las fechas desde el formulario
            hapm_instance.Fecha_compromiso1 = form.cleaned_data.get('Fecha_compromiso1')
            hapm_instance.Fecha_compromiso1_2 = form.cleaned_data.get('Fecha_compromiso1_2')
            hapm_instance.Fecha_compromiso1_3 = form.cleaned_data.get('Fecha_compromiso1_3')
            hapm_instance.Fecha_compromiso1_4 = form.cleaned_data.get('Fecha_compromiso1_4')

            # Guardar la instancia en la base de datos
            hapm_instance.save()

            # Guardar relaciones ManyToMany (miembros del equipo y responsables)
            form.save_m2m()

            for image_file in request.FILES.getlist('Imagen_FallaFun'):
                ImagenFallaFun.objects.create(hapm=hapm_instance, imagen=image_file)
            for image_file in request.FILES.getlist('Imagen_Funcionamiento'):
                ImagenFuncionamiento.objects.create(hapm=hapm_instance, imagen=image_file)
            for image_file in request.FILES.getlist('Imagen_Falla'):
                ImagenFalla.objects.create(hapm=hapm_instance, imagen=image_file)


            for image_id in request.POST.get("delete_images_FallaFun", "").split(","):
                if image_id:
                    ImagenFallaFun.objects.filter(id=image_id).delete()
            for image_id in request.POST.get("delete_images_Funcionamiento", "").split(","):
                if image_id:
                    ImagenFuncionamiento.objects.filter(id=image_id).delete()
            for image_id in request.POST.get("delete_images_Falla", "").split(","):
                if image_id:
                    ImagenFalla.objects.filter(id=image_id).delete()
            

            # Si el formulario es nuevo, enviar el correo
            if es_nuevo:
                # Obtener correos de los miembros del equipo
                emails = [miembro.email for miembro in hapm_instance.miembros_equipo.all()]

                # Preparar el contenido del correo con la categoría e ID
                categoria = hapm_instance.categoria
                id_analisis = hapm_instance.id
                subcategoria = hapm_instance.subcategoria
                area = hapm_instance.area
                subarea = hapm_instance.subarea
                mensaje = f"""
                Has sido asignado a un nuevo proyecto de análisis "5 Por Qué".

                Detalles:
                - ID del Análisis: {id_analisis}
                - Categoría: {categoria}
                - Subcategoria: {subcategoria}
                - Area: {area}
                - Subarea: {subarea}

                Por favor, revisa la plataforma para más detalles.
                """

                # Enviar correo a los miembros del equipo
                try:
                    send_mail(
                        'Nuevo "5 Por Qué" asignado',
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
            return redirect('HAPM', pk=hapm_instance.pk)

        else:
            # Si el formulario no es válido, mostrar errores
            messages.error(request, 'Por favor corrige los errores.')

    else:
        # Si el método es GET (cargar la página por primera vez)
        if hapm_instance:
            areas_seleccionadas = hapm_instance.areas_aplicacion.split(',') if hapm_instance.areas_aplicacion else []
            form = HapmForm(instance=hapm_instance, initial={
                'areas_aplicacion': areas_seleccionadas,
                'Fecha_compromiso1': hapm_instance.Fecha_compromiso1,  # Cargar fechas existentes
                'Fecha_compromiso1_2': hapm_instance.Fecha_compromiso1_2,
                'Fecha_compromiso1_3': hapm_instance.Fecha_compromiso1_3,
                'Fecha_compromiso1_4': hapm_instance.Fecha_compromiso1_4,
            })
        else:
            form = HapmForm()

    # Mostrar el paso 1 solo si ya existe la instancia
    mostrar_paso1 = hapm_instance is not None

    # Obtener todos los miembros del equipo desde la base de datos
    opciones_miembros = MiembroEquipo.objects.all()

    context = {
        'form': form,
        'opciones_area': opciones_area,
        'opciones_subarea': opciones_subarea,
        'opciones_maquina': opciones_maquina,
        'opciones_miembros': opciones_miembros,
        'mostrar_paso1': mostrar_paso1,
        'subcategorias_datos': subcategorias_datos,
        'Imagen_FallaFun': ImagenFallaFun.objects.filter(hapm=hapm_instance),
        'Imagen_Funcionamiento': ImagenFuncionamiento.objects.filter(hapm=hapm_instance),
        'Imagen_Falla': ImagenFalla.objects.filter(hapm=hapm_instance),
    }

    return render(request, 'HAPM/HAPM.html', context)
