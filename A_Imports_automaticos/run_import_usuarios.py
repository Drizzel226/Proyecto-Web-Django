import os
import sys
from django.core.management import call_command

# Asegúrate de que Python encuentre el módulo 'metodologiaups'
sys.path.append('C:\\Users\\ccu\\Desktop\\metodologiaups')

# Establece la configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metodologiaups.settings")

import django
django.setup()

print("Configuración de Django completada...")

# Importa y ejecuta la función
from porque.utils import importar_miembros

print("Función importar_miembros importada. Ejecutando...")

# Ejecutar la función de importar roles
importar_miembros()

print("Sincronización completada.")
