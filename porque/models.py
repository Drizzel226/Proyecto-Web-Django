from django.db import models

class Porque(models.Model):
    categoria = models.CharField(max_length=100)
    subcategoria = models.CharField(max_length=100)
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







from django.db import models

class Paso1(models.Model):
    # Campos existentes
    descripcion_problema = models.TextField("Descripción del problema")
    donde_ocurre = models.TextField("¿Dónde ocurre?")
    como_ocurre = models.TextField("¿Cómo ocurre?")
    cuando_ocurre = models.TextField("¿Cuándo ocurrió?")
    quien_presente = models.TextField("¿Quién estaba presente?")

    senal_antes = models.CharField(
        "Señal antes de que ocurra el problema",
        max_length=100,
        choices=[
            ('alarma', 'Alarma'),
            ('fuga', 'Fuga'),
            ('cavitacion', 'Cavitación'),
            ('ruido', 'Ruido'),
            ('otros', 'Otros'),
            ('nia', 'N/A'),
        ]
    )
    descripcion_senal = models.TextField("Descripción de la señal", blank=True, null=True)

    # Campos adicionales
    falla_funcional = models.TextField("Falla funcional", help_text="Describa la falla funcional que se observó")
    imagen_falla_funcional = models.ImageField(upload_to='imagenes_fallas/', blank=True, null=True)

    def __str__(self):
        return f"Paso 1: {self.descripcion_problema[:50]}..."
