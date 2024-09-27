from django.shortcuts import render, redirect, get_object_or_404
from .forms import PorqueForm
from django.contrib import messages
from google.oauth2 import service_account
from googleapiclient.discovery import build
from .models import MiembroEquipo, Porque
from django.utils.timezone import now


def porque_view(request, pk=None):
    # Configuración de Google Sheets API
    SERVICE_ACCOUNT_FILE = r'C:\Users\Diego Gajardo\Desktop\Proyecto-Web-Django\json.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SPREADSHEET_ID = '1EQxXtEN6arH3AW_7-3AQ0YVf6Q6HXUNth2y1Oy-oVHM'

    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    def obtener_opciones(rango):
        """Función para obtener las opciones desde Google Sheets."""
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=rango).execute()
        return [opcion[0] for opcion in result.get('values', []) if opcion]

    # Obtener las opciones de Google Sheets
    opciones_area = obtener_opciones('Opciones!A2:A')
    opciones_subarea = obtener_opciones('Opciones!B2:B')
    opciones_maquina = obtener_opciones('Opciones!C2:C')

    # Obtener la instancia de Porque si pk es proporcionado
    porque_instance = get_object_or_404(Porque, pk=pk) if pk else None

    if request.method == 'POST':
        form = PorqueForm(request.POST, request.FILES, instance=porque_instance)

        if form.is_valid():
            # Guardar los datos del formulario, incluyendo los "5 porqués"
            porque_instance = form.save(commit=False)
            
            # Guardar la fecha de inicio si es la primera vez
            if not porque_instance.fecha_inicio:
                porque_instance.fecha_inicio = now().date()
                porque_instance.validado1 = form.cleaned_data.get('validado1')
                porque_instance.validado2 = form.cleaned_data.get('validado2')
                porque_instance.validado3 = form.cleaned_data.get('validado3')
                porque_instance.validado4 = form.cleaned_data.get('validado4')
                porque_instance.validado5 = form.cleaned_data.get('validado5')

            # Guardar el campo de causas raíz
            causas_raiz = [
                {
                    "porque1": request.POST.get("porque1"),
                    "validado1": request.POST.get("validado1") == "on",
                    "porque2": request.POST.get("porque2"),
                    "validado2": request.POST.get("validado2") == "on",
                    "porque3": request.POST.get("porque3"),
                    "validado3": request.POST.get("validado3") == "on",
                    "porque4": request.POST.get("porque4"),
                    "validado4": request.POST.get("validado4") == "on",
                    "porque5": request.POST.get("porque5"),
                    "validado5": request.POST.get("validado5") == "on",
                }
            ]
            porque_instance.causas_raiz = causas_raiz
            porque_instance.save()
            form.save_m2m()

            if 'guardar_primera_parte' in request.POST:
                messages.success(request, 'Primera parte guardada con éxito. Ahora puedes completar el Paso 1.')
                return redirect('porque', pk=porque_instance.pk)
            else:
                enviar_a_google_sheets(porque_instance)
                messages.success(request, 'Formulario completo guardado con éxito.')
                return redirect('porque', pk=porque_instance.pk)
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = PorqueForm(instance=porque_instance)

    mostrar_paso1 = porque_instance is not None

    opciones_miembros = MiembroEquipo.objects.all()

    context = {
        'form': form,
        'opciones_area': opciones_area,
        'opciones_subarea': opciones_subarea,
        'opciones_maquina': opciones_maquina,
        'opciones_miembros': opciones_miembros,
        'mostrar_paso1': mostrar_paso1,
    }

    return render(request, 'porque/porque.html', context)


def enviar_a_google_sheets(porque_instance):
    """Función para enviar datos a Google Sheets."""
    try:
        SERVICE_ACCOUNT_FILE = r'C:\Users\Diego Gajardo\Desktop\Proyecto-Web-Django\json.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SPREADSHEET_ID = '1EQxXtEN6arH3AW_7-3AQ0YVf6Q6HXUNth2y1Oy-oVHM'
        RANGE_NAME = 'porque!A2'

        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        fecha_inicio_str = porque_instance.fecha_inicio.isoformat() if porque_instance.fecha_inicio else ''
        fecha_cierre_str = porque_instance.fecha_cierre.isoformat() if porque_instance.fecha_cierre else ''

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
                porque_instance.causas_raiz,
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
