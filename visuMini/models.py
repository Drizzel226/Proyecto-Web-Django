from django.db import models
from MiniProyecto.models import Miniproyecto

class VisuMiniModel(models.Model):
    MiniProyecto = models.OneToOneField(Miniproyecto, on_delete=models.CASCADE)  # Relación 1 a 1 con Miniproyecto
    paso_4 = models.BooleanField(default=False)
    porcentaje = models.IntegerField(default=0)  
    dias = models.IntegerField(null=True, blank=True)  # Asegurarse de que el valor inicial sea un número

    # Otros campos...



from django.db.models.signals import post_save
from django.dispatch import receiver
from MiniProyecto.models import Miniproyecto

@receiver(post_save, sender=Miniproyecto)
def crear_visu5(sender, instance, created, **kwargs):
    if created:
        VisuMiniModel.objects.create(MiniProyecto=instance)



from django.db import models

class Roles(models.Model):
    email = models.EmailField(unique=True)
    rol = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.email} ({self.rol})"

