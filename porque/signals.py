# porque/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MiembroEquipo
from .utils import exportar_miembros

@receiver(post_save, sender=MiembroEquipo)
def actualizar_google_sheets(sender, instance, **kwargs):
    exportar_miembros()  # Actualiza Google Sheets cada vez que un miembro se guarda
