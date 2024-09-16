from django.apps import AppConfig


class PorqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'porque'

# porque/apps.py
from django.apps import AppConfig

class PorqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'porque'

    def ready(self):
        import porque.signals  # Importa las señales cuando la app está lista
