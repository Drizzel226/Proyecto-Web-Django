from django.utils import timezone
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

    def __str__(self):
        return self.nombre



class Paso2(models.Model):
    campo_1 = models.CharField(max_length=100)
    campo2 = models.CharField(max_length=200)
    campo3 = models.TextField()
    # Otros campos necesarios

    def __str__(self):
        return self.campo1
 