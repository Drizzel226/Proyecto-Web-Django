from google.oauth2 import service_account
from googleapiclient.discovery import build
from .models import MiembroEquipo
from django.db import transaction
import time

SERVICE_ACCOUNT_FILE = r'C:\Users\ccu\Desktop\metodologiaups\json.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1EQxXtEN6arH3AW_7-3AQ0YVf6Q6HXUNth2y1Oy-oVHM'
RANGE_NAME = 'Usuarios!A2:C'

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

def importar_miembros():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    rows = result.get('values', [])
    
    # Obtener todos los correos electrónicos existentes en una sola consulta
    existing_emails = set(MiembroEquipo.objects.values_list('email', flat=True))
    
    new_members = []
    for row in rows:
        if len(row) >= 3:  # Asegurarse de que la fila tiene suficientes elementos
            email = row[2]
            if email not in existing_emails:
                new_members.append(MiembroEquipo(nombre=row[1], email=email))
    
    # Crear todos los nuevos miembros en una sola operación de base de datos
    with transaction.atomic():
        MiembroEquipo.objects.bulk_create(new_members)

def exportar_miembros():
    miembros = MiembroEquipo.objects.all().values_list('id', 'nombre', 'email')
    
    batch_size = 500  # Aumentamos el tamaño del lote
    for i in range(0, len(miembros), batch_size):
        batch = miembros[i:i+batch_size]
        range_name = f'Usuarios!A{i+2}:C{i+len(batch)+1}'
        body = {'values': list(batch)}
        
        sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=range_name,
            valueInputOption='RAW',
            body=body
        ).execute()
        
        time.sleep(0.5)  # Reducimos el tiempo de espera entre solicitudes