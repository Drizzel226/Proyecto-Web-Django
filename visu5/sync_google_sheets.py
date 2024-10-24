from google.oauth2 import service_account
from googleapiclient.discovery import build
from .models import Roles
from django.db import transaction

# Configuración de la cuenta de servicio y la hoja de cálculo
SERVICE_ACCOUNT_FILE = r'C:\Users\ccu\Desktop\metodologiaups\json.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1EQxXtEN6arH3AW_7-3AQ0YVf6Q6HXUNth2y1Oy-oVHM'
RANGE_NAME = 'Auditores!A2:B'  # Asegúrate de que este rango incluya las columnas de 'mail' y 'Rol'

# Autenticación con Google Sheets
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

def importar_roles():
    # Obtener los datos de la hoja de cálculo
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    rows = result.get('values', [])

    # Extraer los emails y roles de la hoja
    google_data = {row[0]: int(row[1]) if len(row) > 1 and row[1].isdigit() else 0 for row in rows}

    # Obtener todos los emails existentes en la base de datos
    existing_roles = Roles.objects.all()
    existing_emails = {role.email: role for role in existing_roles}

    # Preparar listas para crear, actualizar y eliminar roles
    roles_to_create = []
    roles_to_update = []
    emails_in_google_sheet = set(google_data.keys())

    for email, rol in google_data.items():
        if email in existing_emails:
            # Actualizar el rol si ha cambiado
            role_obj = existing_emails[email]
            if role_obj.rol != rol:
                role_obj.rol = rol
                roles_to_update.append(role_obj)
        else:
            # Crear nuevos roles que no están en la base de datos
            roles_to_create.append(Roles(email=email, rol=rol))

    # Identificar los roles que deben ser eliminados
    emails_to_delete = existing_emails.keys() - emails_in_google_sheet
    roles_to_delete = [existing_emails[email] for email in emails_to_delete]

    # Realizar las operaciones en una transacción atómica
    with transaction.atomic():
        # Crear nuevos roles
        if roles_to_create:
            Roles.objects.bulk_create(roles_to_create)
        
        # Actualizar roles existentes
        if roles_to_update:
            Roles.objects.bulk_update(roles_to_update, ['rol'])
        
        # Eliminar roles que ya no están en la hoja de cálculo
        if roles_to_delete:
            Roles.objects.filter(id__in=[role.id for role in roles_to_delete]).delete()

    print("Sincronización de roles completada.")
