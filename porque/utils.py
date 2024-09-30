from google.oauth2 import service_account
from googleapiclient.discovery import build
from .models import MiembroEquipo

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
    
    for row in rows:
        email = row[2]
        if not MiembroEquipo.objects.filter(email=email).exists():
            MiembroEquipo.objects.create(nombre=row[1], email=email)


import time

def exportar_miembros():
    miembros = MiembroEquipo.objects.all()
    values = [[miembro.id, miembro.nombre, miembro.email] for miembro in miembros]
    body = {'values': values}

    for i in range(0, len(values), 50):  # Envía los datos en bloques de 10
        batch = values[i:i+50]
        range_name = f'Usuarios!A{i+2}:C{i+len(batch)+1}'  # Formato correcto de rango
        body = {'values': batch}
        sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=range_name,
            valueInputOption='RAW',
            body=body
        ).execute()
        time.sleep(1)  # Espera para evitar superar la cuota


