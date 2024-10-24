import os
from django.core.management import call_command

# Establece la configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metodologiaups.settings")

import django
django.setup()

print("Configuración de Django completada...")

# Importa y ejecuta la función
from visu5.sync_google_sheets import importar_roles

print("Función importar_roles importada. Ejecutando...")

# Ejecutar la función de importar roles
importar_roles()

print("Sincronización completada.")
