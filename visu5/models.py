from django.db import models
from porque.models import Porque

class Visu5Model(models.Model):
    porque = models.OneToOneField(Porque, on_delete=models.CASCADE)  # Relación 1 a 1 con Porque
    paso_4 = models.BooleanField(default=False)
    porcentaje = models.IntegerField(default=0)  
    dias = models.IntegerField(default=0)  # Asegurarse de que el valor inicial sea un número

    # Otros campos...



from django.db.models.signals import post_save
from django.dispatch import receiver
from porque.models import Porque

@receiver(post_save, sender=Porque)
def crear_visu5(sender, instance, created, **kwargs):
    if created:
        Visu5Model.objects.create(porque=instance)



from django.db import models

class Roles(models.Model):
    email = models.EmailField(unique=True)
    rol = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.email} ({self.rol})"

