from django.db import models
from Kaizen.models import Kaizen

class VisuKaiModel(models.Model):
    Kaizen = models.OneToOneField(Kaizen, on_delete=models.CASCADE)  # Relación 1 a 1 con Miniproyecto
    paso_4 = models.BooleanField(default=False)
    porcentaje = models.IntegerField(default=0)  
    dias = models.IntegerField(null=True, blank=True)  # Asegurarse de que el valor inicial sea un número

    # Otros campos...



from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Kaizen)
def crear_visu5(sender, instance, created, **kwargs):
    if created:
        VisuKaiModel.objects.create(Kaizen=instance)

