from django.shortcuts import render, redirect
from .forms import PorqueForm, Paso2Form
from django.contrib import messages
from google.oauth2 import service_account
from googleapiclient.discovery import build
from .models import MiembroEquipo





def porque_view(request):
    SERVICE_ACCOUNT_FILE = 'C:\\Users\\ccu\\Desktop\\Proyecto\\Random\\json.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SPREADSHEET_ID = '1EQxXtEN6arH3AW_7-3AQ0YVf6Q6HXUNth2y1Oy-oVHM'
    
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    def obtener_opciones(rango):
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=rango).execute()
        return [opcion[0] for opcion in result.get('values', []) if opcion]

    opciones_area = obtener_opciones('Opciones!A2:A')
    opciones_subarea = obtener_opciones('Opciones!B2:B')
    opciones_maquina = obtener_opciones('Opciones!C2:C')

    if request.method == 'POST':
        form = PorqueForm(request.POST)
        if form.is_valid():
            porque_instance = form.save()
            try:
                enviar_a_google_sheets(porque_instance)
                messages.success(request, 'Formulario enviado con éxito y datos guardados en Google Sheets.')
            except Exception as e:
                messages.error(request, f'El formulario fue guardado, pero ocurrió un error al enviar a Google Sheets: {e}')
            return redirect('paso2')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = PorqueForm()

    # Obtener opciones de MiembroEquipo y pasarlas al template
    opciones_miembros = MiembroEquipo.objects.all()

    context = {
        'form': form,
        'opciones_area': opciones_area,
        'opciones_subarea': opciones_subarea,
        'opciones_maquina': opciones_maquina,
        'opciones_miembros': opciones_miembros,
    }

    return render(request, 'porque/porque.html', context)





def enviar_a_google_sheets(porque_instance):
    try:
        SERVICE_ACCOUNT_FILE = 'C:\\Users\\ccu\\Desktop\\Proyecto\\Random\\json.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SPREADSHEET_ID = '1EQxXtEN6arH3AW_7-3AQ0YVf6Q6HXUNth2y1Oy-oVHM'
        RANGE_NAME = 'porque!A2'

        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        fecha_inicio_str = porque_instance.fecha_inicio.isoformat()
        fecha_cierre_str = porque_instance.fecha_cierre.isoformat()

        # Convertir miembros_equipo a una cadena
        miembros_equipo_str = ', '.join([miembro.nombre for miembro in porque_instance.miembros_equipo.all()])

        values = [
            [
                porque_instance.id,
                porque_instance.area,
                porque_instance.subarea,
                porque_instance.maquina,
                miembros_equipo_str,
                porque_instance.pilar,
                porque_instance.impacto,
                porque_instance.kpi_iceo,
                porque_instance.kpi_secundario,
                fecha_inicio_str,
                fecha_cierre_str,
            ],
        ]

        body = {'values': values}
        result = sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption="RAW",
            body=body
        ).execute()

        print(f"Dato enviado con éxito a Google Sheets: {result}")

    except Exception as e:
        print(f"Error al enviar datos a Google Sheets: {e}")




def paso2_view(request):
    if request.method == 'POST':
        form = Paso2Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paso 2 completado con éxito.')
            return redirect('paso2')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = Paso2Form()

    return render(request, 'porque/paso2.html', {'form': form})



"""
def enviar_a_google_sheets(data):
    # Ruta al archivo JSON con las credenciales
    SERVICE_ACCOUNT_FILE = 'C:\\Users\\ccu\\Desktop\\Proyecto\\Random\\json.json'

    # Alcances que se requieren
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # Credenciales
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # ID de tu Google Sheet
    SPREADSHEET_ID = '1EQxXtEN6arH3AW_7-3AQ0YVf6Q6HXUNth2y1Oy-oVHM'
    RANGE_NAME = 'porque!A2'  # El rango donde se añadirán los datos

    # Datos que se van a agregar (ordenados en la misma secuencia que las columnas)
    values = [
        [
            data['nombre'],
            data['email'],
            data['asunto'],
            data['mensaje'],
            data['categoria'],
            data['prioridad'],
            data['seguimiento'],
            # Puedes agregar otros campos si es necesario
        ],
    ]

    # Cuerpo de la petición
    body = {
        'values': values
    }

    # Llamar a la API para agregar la fila
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption="RAW",
        body=body
    ).execute()









"""