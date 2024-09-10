from django.shortcuts import render, redirect
from .forms import PorqueForm, Paso2Form
from django.contrib import messages
from google.oauth2 import service_account
from googleapiclient.discovery import build





def porque_view(request):
    if request.method == 'POST':
        form = PorqueForm(request.POST)
        if form.is_valid():
            form.save()

            # Enviar los datos a Google Sheets y manejar errores
            try:
                enviar_a_google_sheets(form.cleaned_data)
                messages.success(request, 'Formulario enviado con éxito y datos guardados en Google Sheets.')
            except Exception as e:
                messages.error(request, f'El formulario fue guardado, pero ocurrió un error al enviar a Google Sheets: {e}')

            return redirect('porque')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = PorqueForm()

    return render(request, 'porque/porque.html', {'form': form})

def enviar_a_google_sheets(data):
    try:
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

        # Convierte las fechas a formato de cadena
        fecha_inicio_str = data['fecha_inicio'].isoformat()
        fecha_cierre_str = data['fecha_cierre'].isoformat()

        # Datos que se van a agregar
        values = [
            [
                data['id'],
                data['area'],
                data['linea'],
                data['subcategoria'],
                data['miembros_equipo'],
                data['pilar'],
                data['impacto'],
                data['kpi_iceo'],
                data['kpi_secundario'],
                fecha_inicio_str,
                fecha_cierre_str,
            ],
        ]

        # Cuerpo de la petición
        body = {
            'values': values
        }

        # Llamar a la API para agregar la fila
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
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