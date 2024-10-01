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
            # Guardar la instancia del formulario pero sin guardarla aún en la BD
            porque_instance = form.save(commit=False)

            # Asignar la fecha de inicio si es la primera vez que se guarda
            if not porque_instance.fecha_inicio:
                porque_instance.fecha_inicio = now().date()

            # Ahora sí guardar la instancia en la base de datos
            porque_instance.save()  # Guardar para obtener el ID

            # Guardar relaciones ManyToMany
            form.save_m2m()

            # Mensaje de éxito y redirigir con el ID
            messages.success(request, 'Se a guardo con éxito. Puedes continuar.')
            return redirect('porque', pk=porque_instance.pk)  # Redirigir a la misma página con el ID

        else:
            # Si el formulario no es válido, mostrar errores
            messages.error(request, 'Por favor corrige los errores.')

    else:
        # Si el método es GET (cargar la página por primera vez)
        form = PorqueForm(instance=porque_instance)

    mostrar_paso1 = porque_instance is not None  # Mostrar el paso 1 solo si ya existe la instancia

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
