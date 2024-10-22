python manage.py shell
from porque.utils import importar_miembros
importar_miembros()
from visu5.sync_google_sheets import importar_roles
importar_roles()







                            <!-- Ícono con popover que mostrará la imagen -->
                            <div class="popover-container">
                                <i class="fas fa-question-circle"></i>
                                <div class="popover-content">
                                    <img src="{% static 'images/logo.png' %}" alt="Descripción de la imagen" style="width: 300px;">
                                </div>
                            </div>


views.py

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
