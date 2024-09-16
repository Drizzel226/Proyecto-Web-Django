from django.shortcuts import render, redirect, get_object_or_404
from .forms import PorqueForm
from django.contrib import messages
from google.oauth2 import service_account
from googleapiclient.discovery import build
from .models import MiembroEquipo, Porque
from django.utils.timezone import now

def porque_view(request, pk=None):
    SERVICE_ACCOUNT_FILE = 'C:\\Users\\ccu\\Desktop\\Proyecto\\Random\\json.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SPREADSHEET_ID = '1EQxXtEN6arH3AW_7-3AQ0YVf6Q6HXUNth2y1Oy-oVHM'

    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    def obtener_opciones(rango):
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=rango).execute()
        return [opcion[0] for opcion in result.get('values', []) if opcion]

    opciones_area = obtener_opciones('Opciones!A2:A')
    opciones_subarea = obtener_opciones('Opciones!B2:B')
    opciones_maquina = obtener_opciones('Opciones!C2:C')

    # Obtener la instancia del objeto Porque si existe, o crear uno nuevo si no
    porque_instance = get_object_or_404(Porque, pk=pk) if pk else None

    if request.method == 'POST':
        form = PorqueForm(request.POST, request.FILES, instance=porque_instance)
        
        if form.is_valid():
            porque_instance = form.save()
            try:
                enviar_a_google_sheets(porque_instance)
                messages.success(request, 'Formulario guardado con éxito y datos enviados a Google Sheets.')
            except Exception as e:
                messages.error(request, f'El formulario fue guardado, pero ocurrió un error al enviar a Google Sheets: {e}')
            return redirect('porque', pk=porque_instance.pk)
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = PorqueForm(instance=porque_instance)

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

        miembros_equipo_str = ', '.join([miembro.nombre for miembro in porque_instance.miembros_equipo.all()])

        values = [
            [
                porque_instance.id,
                porque_instance.categoria,
                porque_instance.subcategoria,
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
