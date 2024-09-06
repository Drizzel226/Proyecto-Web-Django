# myapp/models.py

from django.db import models


class Porque(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    categoria = models.CharField(max_length=50)
    prioridad = models.CharField(max_length=20)
    seguimiento = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asunto} - {self.fecha_creacion}"
    


class Paso2(models.Model):
    campo_1 = models.CharField(max_length=100)
    campo2 = models.CharField(max_length=200)
    campo3 = models.TextField()
    # Otros campos necesarios

    def __str__(self):
        return self.campo1
    
class Paso3(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.CharField(max_length=200)
    campo3 = models.TextField()
    # Otros campos necesarios

    def __str__(self):
        return self.campo1

class Paso4(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.CharField(max_length=200)
    campo3 = models.TextField()
    # Otros campos necesarios

    def __str__(self):
        return self.campo1

class Paso5(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.CharField(max_length=200)
    campo3 = models.TextField()
    # Otros campos necesarios

    def __str__(self):
        return self.campo1