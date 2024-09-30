from django.shortcuts import render, redirect, get_object_or_404
from .forms import PorqueForm
from .models import Porque, MiembroEquipo
from django.contrib import messages
from django.utils.timezone import now
from google.oauth2 import service_account
from googleapiclient.discovery import build

def porque_view(request, pk=None):
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

    # Obtener las opciones de Google Sheets
    opciones_area = obtener_opciones('Opciones!A2:A')
    opciones_subarea = obtener_opciones('Opciones!B2:B')
    opciones_maquina = obtener_opciones('Opciones!C2:C')

    # Obtener la instancia de Porque si pk es proporcionado
    porque_instance = get_object_or_404(Porque, pk=pk) if pk else None

    if request.method == 'POST':
        form = PorqueForm(request.POST, request.FILES, instance=porque_instance)

        if form.is_valid():
            # Guardar los datos del formulario
            porque_instance = form.save(commit=False)

            # Guardar la fecha de inicio si es la primera vez
            if not porque_instance.fecha_inicio:
                porque_instance.fecha_inicio = now().date()

            porque_instance.save()
            form.save_m2m()

            if 'guardar_primera_parte' in request.POST:
                messages.success(request, 'Primera parte guardada con éxito. Ahora puedes completar el Paso 1.')
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
