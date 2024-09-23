from django.db import models

from django.db import models

class Porque(models.Model):
    # Campos existentes
    categoria = models.CharField(max_length=100, blank=True, null=True)
    subcategoria = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    subarea = models.CharField(max_length=100, blank=True, null=True)
    maquina = models.CharField(max_length=100, blank=True, null=True)
    miembros_equipo = models.ManyToManyField('MiembroEquipo')
    pilar = models.CharField(max_length=100, blank=True, null=True)
    impacto = models.TextField(blank=True, null=True)
    kpi_iceo = models.CharField(max_length=100, blank=True, null=True)
    kpi_secundario = models.CharField(max_length=100, blank=True, null=True)
    fecha_inicio = models.DateField(auto_now_add=True, blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)

    # Campos adicionales
    que_ocurre = models.TextField("¿Qué ocurre? ¿En qué parte de la máquina o material se visualiza el problema?", blank=True, null=True)
    como_ocurre = models.TextField("¿Cómo ocurre? Describir desde el punto de vista físico el mecanismo de acción visibilizado en el momento.", blank=True, null=True)
    donde_ocurre = models.TextField("¿Dónde ocurre? Producto, equipo, zona de la máquina, etc.", blank=True, null=True)
    cuando_ocurre = models.TextField("¿Cuándo ocurrió? Producción, arranque, saneado, cambio de formato, mantención, etc.", blank=True, null=True)
    quien_presente = models.TextField("¿Quién estaba presente cuando ocurrió? ¿El problema pasa en todos los turnos?", blank=True, null=True)

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
        ],
        blank=True, null=True
    )
    descripcion_senal = models.TextField("Descripción de la señal", blank=True, null=True)
    falla_funcional = models.TextField("Falla funcional", blank=True, null=True)
    imagen_falla_funcional = models.ImageField(upload_to='imagenes_fallas/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Si es una edición
            original = Porque.objects.get(pk=self.pk)
            
            # Verificar que la fecha de inicio no se cambie
            if original.fecha_inicio and self.fecha_inicio != original.fecha_inicio:
                raise ValueError("La fecha de inicio no puede ser cambiada una vez establecida.")
            
        super().save(*args, **kwargs)

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







