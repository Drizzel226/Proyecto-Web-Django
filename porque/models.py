from django.db import models

class Porque(models.Model):
    area = models.CharField(max_length=100)
    subarea = models.CharField(max_length=100)
    maquina = models.CharField(max_length=100)
    miembros_equipo = models.ManyToManyField('MiembroEquipo')
    pilar = models.CharField(max_length=100)
    impacto = models.TextField()
    kpi_iceo = models.CharField(max_length=100)
    kpi_secundario = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_cierre = models.DateField()

    def __str__(self):
        return f"{self.area}"


class MiembroEquipo(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MiembroEquipo
from .utils import exportar_miembros

@receiver(post_save, sender=MiembroEquipo)
def actualizar_google_sheets(sender, instance, **kwargs):
    exportar_miembros()  # Actualiza Google Sheets cada vez que un miembro se guarda

