from google.oauth2 import service_account
from googleapiclient.discovery import build
from .models import Roles
from django.db import transaction

SERVICE_ACCOUNT_FILE = r'C:\Users\ccu\Desktop\metodologiaups\json.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1EQxXtEN6arH3AW_7-3AQ0YVf6Q6HXUNth2y1Oy-oVHM'
RANGE_NAME = 'Auditores!A2:B'  # Asegúrate de que este rango incluya las columnas de 'mail' y 'Rol'

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

def importar_roles():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    rows = result.get('values', [])
    
    existing_emails = set(Roles.objects.values_list('email', flat=True))
    
    new_roles = []
    for row in rows:
        if len(row) >= 2:  # Asegúrate de que la fila tiene suficientes elementos (email, rol)
            email = row[0]
            try:
                rol = int(row[1])  # Convertir el rol a entero
            except ValueError:
                rol = 0  # Si no se puede convertir, asignar un rol por defecto de 0

            if email not in existing_emails:
                new_roles.append(Roles(email=email, rol=rol))
    
    # Crear todos los nuevos roles en una sola operación de base de datos
    with transaction.atomic():
        Roles.objects.bulk_create(new_roles)
