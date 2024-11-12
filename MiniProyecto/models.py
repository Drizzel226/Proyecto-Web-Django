from django.db import models


class Miniproyecto(models.Model):
    # Campos existentes
    Nombre_MP = models.TextField(max_length=100, blank=True, null=True)
    costo = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True, default="0")
    ahorro = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True, default="0")
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

    # Paso 1
    que_ocurre = models.TextField("¿Qué ocurre? ¿En qué parte de la máquina o material se visualiza el problema?", blank=True, null=True)
    donde_ocurre = models.TextField("¿Dónde ocurre? Producto, equipo, zona de la máquina, etc.", blank=True, null=True)
    como_ocurre = models.TextField("¿Cómo ocurre? Describir desde el punto de vista físico el mecanismo de acción visibilizado en el momento.", blank=True, null=True)
    cuando_ocurre = models.TextField("¿Cuándo ocurrió? Producción, arranque, saneado, cambio de formato, mantención, etc.", blank=True, null=True)
    quien_intervino = models.TextField("¿Quién pudo influir o interviene?", blank=True, null=True)
    perdida = models.TextField("¿Cuánto es la pérdida asociada? (horas, kilos, cajas, botellas, dinero, etc)", blank=True, null=True)
    resumen = models.TextField("Resumen del problema", blank=True, null=True)
    imagen_falla_funcional = models.ImageField(upload_to='imagenes_fallas/', null=True, blank=True)

    # Paso 2
    condicion_basica = models.TextField("¿Existe un estándar (procedimiento/instructivo/formato definido)?, ¿Es conocido por todos, existe un entrenamiento (Registro de capacitación/LUP) ?¿Cumple mantenciones preventivas?", blank=True, null=True)
    imagen_funcionamiento = models.ImageField(upload_to='imagenes_funcionamiento/', blank=True, null=True)



    # PASO 3

    ISHIKAWA = models.CharField(
        max_length=100,
        choices=[
            ('Máquina', 'Máquina'),
            ('Método', 'Método'),
            ('Medio Ambiente', 'Medio Ambiente'),
            ('Material', 'Material'),
            ('Medición', 'Medición'),
            ('Mano de Obra', 'Mano de Obra'),
  
        ],
        verbose_name="Escoja una de las 6 M",   
        blank=True, null=True,
        
    )
    desarrollo = models.TextField("Describa causa raíz", blank=True, null=True)

    
    
    # PASO 4


    Accion_Preventiva = models.TextField(blank=True, null=True)
    Accion_Preventiva_2 = models.TextField(blank=True, null=True)
    Accion_Preventiva_3 = models.TextField(blank=True, null=True)
    Accion_Preventiva_4 = models.TextField(blank=True, null=True)

    Responsable2 = models.ManyToManyField('MiembroEquipo', related_name="responsable2", blank=True)
    Responsable2_2 = models.ManyToManyField('MiembroEquipo', related_name="responsable2_2", blank=True)
    Responsable2_3 = models.ManyToManyField('MiembroEquipo', related_name="responsable2_3", blank=True)
    Responsable2_4 = models.ManyToManyField('MiembroEquipo', related_name="responsable2_4", blank=True)

    Fecha_inicio2 = models.DateField(blank=True, null=True)
    Fecha_inicio2_2 = models.DateField(blank=True, null=True)
    Fecha_inicio2_3 = models.DateField(blank=True, null=True)
    Fecha_inicio2_4 = models.DateField(blank=True, null=True)

    Fecha_compromiso2 = models.DateField(blank=True, null=True)
    Fecha_compromiso2_2 = models.DateField(blank=True, null=True)
    Fecha_compromiso2_3 = models.DateField(blank=True, null=True)
    Fecha_compromiso2_4 = models.DateField(blank=True, null=True)

    ESTADO_OPCIONES = [
    ('Pendiente', 'Pendiente'),
    ('Cerrada', 'Cerrada'),
    ]
    estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_2 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_3 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_4 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')

    Fecha_cierre_paso4 = models.DateField(blank=True, null=True)
    Fecha_cierre_paso4_2 = models.DateField(blank=True, null=True)
    Fecha_cierre_paso4_3 = models.DateField(blank=True, null=True)
    Fecha_cierre_paso4_4 = models.DateField(blank=True, null=True)
    



    # PASO 5

    Estandarizacion = models.TextField(blank=True, null=True)
    Responsable3 = models.ManyToManyField('MiembroEquipo', related_name="responsable3", blank=True)
    Fecha_compromiso3 = models.DateField(blank=True, null=True)

    Estandarizacion_2 = models.TextField(blank=True, null=True)
    Responsable3_2 = models.ManyToManyField('MiembroEquipo', related_name="responsable3_2", blank=True)
    Fecha_compromiso3_2 = models.DateField(blank=True, null=True)

    Estandarizacion_3 = models.TextField(blank=True, null=True)
    Responsable3_3 = models.ManyToManyField('MiembroEquipo', related_name="responsable3_3", blank=True)
    Fecha_compromiso3_3 = models.DateField(blank=True, null=True)
    
    Estandarizacion_4 = models.TextField(blank=True, null=True)
    Responsable3_4 = models.ManyToManyField('MiembroEquipo', related_name="responsable3_4", blank=True)
    Fecha_compromiso3_4 = models.DateField(blank=True, null=True)


    Expansion = models.TextField(blank=True, null=True)
    Responsable4 = models.ManyToManyField('MiembroEquipo', related_name="responsable4", blank=True)
    Fecha_compromiso4 = models.DateField(blank=True, null=True)

    Expansion_2 = models.TextField(blank=True, null=True)
    Responsable4_2 = models.ManyToManyField('MiembroEquipo', related_name="responsable4_2", blank=True)
    Fecha_compromiso4_2 = models.DateField(blank=True, null=True)

    Expansion_3 = models.TextField(blank=True, null=True)
    Responsable4_3 = models.ManyToManyField('MiembroEquipo', related_name="responsable4_3", blank=True)
    Fecha_compromiso4_3 = models.DateField(blank=True, null=True)

    Expansion_4 = models.TextField(blank=True, null=True)
    Responsable4_4 = models.ManyToManyField('MiembroEquipo', related_name="responsable4_4", blank=True)
    Fecha_compromiso4_4 = models.DateField(blank=True, null=True)

    areas_aplicacion = models.CharField(max_length=500, blank=True, null=True)


    puntaje = models.IntegerField(null=True, blank=True)




class MiembroEquipo(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import exportar_miembros

@receiver(post_save, sender=MiembroEquipo)
def actualizar_google_sheets(sender, instance, **kwargs):
    exportar_miembros()  # Actualiza Google Sheets cada vez que un miembro se guarda


# models.py

from django.db import models

class ImagenMiniproyecto(models.Model):
    miniproyecto = models.ForeignKey(Miniproyecto, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_miniproyectos/')

    def __str__(self):
        return f"Imagen para {self.miniproyecto.Nombre_MP}"
    
class ImagenFuncionamiento(models.Model):
    miniproyecto = models.ForeignKey(Miniproyecto, related_name='imagenes_funcionamiento', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_funcionamiento/')
    
    def __str__(self):
        return f"Imagen Funcionamiento para {self.miniproyecto.Nombre_MP}"
    
class ImagenAntes(models.Model):
    miniproyecto = models.ForeignKey(Miniproyecto, related_name='imagenes_antes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_antes/')
    
    def __str__(self):
        return f"Imagen Antes para {self.miniproyecto.Nombre_MP}"

class ImagenDespues(models.Model):
    miniproyecto = models.ForeignKey(Miniproyecto, related_name='imagenes_despues', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_despues/')
    
    def __str__(self):
        return f"Imagen Después para {self.miniproyecto.Nombre_MP}"