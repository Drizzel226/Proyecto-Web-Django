from django.db import models


class Kaizen(models.Model):
    # Campos existentes
    Nombre_Kaizen = models.TextField(max_length=100, blank=True, null=True)
    ahorro = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True, default="0")
    categoria = models.CharField(max_length=100, blank=True, null=True)
    subcategoria = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    subarea = models.CharField(max_length=100, blank=True, null=True)
    maquina = models.CharField(max_length=100, blank=True, null=True)
    miembros_equipo = models.ManyToManyField('MiembroEquipo')
    lider = models.ManyToManyField('MiembroEquipo', related_name="lider", blank=True)
    pilar = models.CharField(max_length=100, blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    kpi_iceo = models.CharField(max_length=100, blank=True, null=True)
    kpi_secundario = models.CharField(max_length=100, blank=True, null=True)
    valor_inicial = models.CharField(max_length=100, blank=True, null=True)
    valor_propuesto_final = models.CharField(max_length=100, blank=True, null=True)
    valor_real_final = models.CharField(max_length=100, blank=True, null=True)
    fecha_inicio = models.DateField(auto_now_add=True, blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)

    # Deployment de Perdida y Objetivo SMART
    Deployment = models.TextField("Deployment de perdidas", blank=True, null=True)
    especifico = models.TextField(blank=True, null=True)
    medible = models.TextField(blank=True, null=True)
    alcanzable = models.TextField(blank=True, null=True)
    realista = models.TextField(blank=True, null=True)
    tiempo = models.TextField(blank=True, null=True)


    # Paso 1
    descripcion = models.TextField("Descripción del problema", blank=True, null=True)
    imagen_falla_funcional = models.ImageField(upload_to='imagenes_fallas/', null=True, blank=True)
    
    RESPUESTA_CHOICES = [
        ('visual', 'Visual'),
        ('unificado', 'Unificar'),
        ('5W & H', '5W & H'),
        ('otros, especificar', 'Otros, especifico'),
    ]

    seleccion = models.CharField(
        "Selección:",
        max_length=20,
        choices=RESPUESTA_CHOICES,
        default='no_aplica',
        blank=False,
        null=True
    )


    # Paso 2
    condicion_basica = models.TextField("Entender los principios de funcionamiento y parámetros -> describir el modo de falla -> restaurar las condiciones básicas (relacionadas)", blank=True, null=True)
    imagen_funcionamiento = models.ImageField(upload_to='imagenes_funcionamiento/', blank=True, null=True)

    Respuesta = [
        ('principio de funcionamiento', 'Principio de funcionamiento'),
        ('verificar parametro', 'Verificar parámetros'),
        ('layouts', 'Layout'),
        ('grafica de recorrido', 'Gráfica de recorrido'),
        ('otros, especificar', 'Otros, especifico'),
    ]

    seleccion_paso2 = models.CharField(
        "Selección:",
        max_length=30,
        choices=Respuesta,
        default='no_aplica',
        blank=False,
        null=True
    )


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
    desarrollo = models.TextField("Identificar posibles causas basados en el(los) modo(s) de falla(s) -> definir la hipótesis y verificar -> ligar la(s) causa(s) raíz con las 6M's", blank=True, null=True)

    modo_falla_paso3 = models.TextField("Modo de Falla", blank=True, null=True)
    porque1 = models.TextField("¿POR QUÉ? (1)", blank=True, null=True)
    porque2 = models.TextField("¿POR QUÉ? (2)", blank=True, null=True)
    porque3 = models.TextField("¿POR QUÉ? (3)", blank=True, null=True)
    porque4 = models.TextField("¿POR QUÉ? (4)", blank=True, null=True)
    porque5 = models.TextField("¿POR QUÉ? (5)", blank=True, null=True)
    porque6 = models.TextField("¿POR QUÉ? (6)", blank=True, null=True)
    porque7 = models.TextField("¿POR QUÉ? (7)", blank=True, null=True)
    
    modo_falla_paso3_2 = models.TextField("Modo de Falla", blank=True, null=True)
    porque1_2 = models.TextField("¿POR QUÉ? (1)", blank=True, null=True)
    porque2_2 = models.TextField("¿POR QUÉ? (2)", blank=True, null=True)
    porque3_2 = models.TextField("¿POR QUÉ? (3)", blank=True, null=True)
    porque4_2 = models.TextField("¿POR QUÉ? (4)", blank=True, null=True)
    porque5_2 = models.TextField("¿POR QUÉ? (5)", blank=True, null=True)
    porque6_2 = models.TextField("¿POR QUÉ? (6)", blank=True, null=True)
    porque7_2 = models.TextField("¿POR QUÉ? (7)", blank=True, null=True)
    
    modo_falla_paso3_3 = models.TextField("Modo de Falla", blank=True, null=True)
    porque1_3 = models.TextField("¿POR QUÉ? (1)", blank=True, null=True)
    porque2_3 = models.TextField("¿POR QUÉ? (2)", blank=True, null=True)
    porque3_3 = models.TextField("¿POR QUÉ? (3)", blank=True, null=True)
    porque4_3 = models.TextField("¿POR QUÉ? (4)", blank=True, null=True)
    porque5_3 = models.TextField("¿POR QUÉ? (5)", blank=True, null=True)
    porque6_3 = models.TextField("¿POR QUÉ? (6)", blank=True, null=True)
    porque7_3 = models.TextField("¿POR QUÉ? (7)", blank=True, null=True)

    modo_falla_paso3_4 = models.TextField("Modo de Falla", blank=True, null=True)
    porque1_4 = models.TextField("¿POR QUÉ? (1)", blank=True, null=True)
    porque2_4 = models.TextField("¿POR QUÉ? (2)", blank=True, null=True)
    porque3_4 = models.TextField("¿POR QUÉ? (3)", blank=True, null=True)
    porque4_4 = models.TextField("¿POR QUÉ? (4)", blank=True, null=True)
    porque5_4 = models.TextField("¿POR QUÉ? (5)", blank=True, null=True)
    porque6_4 = models.TextField("¿POR QUÉ? (6)", blank=True, null=True)
    porque7_4 = models.TextField("¿POR QUÉ? (7)", blank=True, null=True)

    modo_falla_paso3_5 = models.TextField("Modo de Falla", blank=True, null=True)
    porque1_5 = models.TextField("¿POR QUÉ? (1)", blank=True, null=True)
    porque2_5 = models.TextField("¿POR QUÉ? (2)", blank=True, null=True)
    porque3_5 = models.TextField("¿POR QUÉ? (3)", blank=True, null=True)
    porque4_5 = models.TextField("¿POR QUÉ? (4)", blank=True, null=True)
    porque5_5 = models.TextField("¿POR QUÉ? (5)", blank=True, null=True)
    porque6_5 = models.TextField("¿POR QUÉ? (6)", blank=True, null=True)
    porque7_5 = models.TextField("¿POR QUÉ? (7)", blank=True, null=True)

    modo_falla_paso3_6 = models.TextField("Modo de Falla", blank=True, null=True)
    porque1_6 = models.TextField("¿POR QUÉ? (1)", blank=True, null=True)
    porque2_6 = models.TextField("¿POR QUÉ? (2)", blank=True, null=True)
    porque3_6 = models.TextField("¿POR QUÉ? (3)", blank=True, null=True)
    porque4_6 = models.TextField("¿POR QUÉ? (4)", blank=True, null=True)
    porque5_6 = models.TextField("¿POR QUÉ? (5)", blank=True, null=True)
    porque6_6 = models.TextField("¿POR QUÉ? (6)", blank=True, null=True)
    porque7_6 = models.TextField("¿POR QUÉ? (7)", blank=True, null=True)

    modo_falla_paso3_7 = models.TextField("Modo de Falla", blank=True, null=True)
    porque1_7 = models.TextField("¿POR QUÉ? (1)", blank=True, null=True)
    porque2_7 = models.TextField("¿POR QUÉ? (2)", blank=True, null=True)
    porque3_7 = models.TextField("¿POR QUÉ? (3)", blank=True, null=True)
    porque4_7 = models.TextField("¿POR QUÉ? (4)", blank=True, null=True)
    porque5_7 = models.TextField("¿POR QUÉ? (5)", blank=True, null=True)
    porque6_7 = models.TextField("¿POR QUÉ? (6)", blank=True, null=True)
    porque7_7 = models.TextField("¿POR QUÉ? (7)", blank=True, null=True)

    modo_falla_paso3_8 = models.TextField("Modo de Falla", blank=True, null=True)
    porque1_8 = models.TextField("¿POR QUÉ? (1)", blank=True, null=True)
    porque2_8 = models.TextField("¿POR QUÉ? (2)", blank=True, null=True)
    porque3_8 = models.TextField("¿POR QUÉ? (3)", blank=True, null=True)
    porque4_8 = models.TextField("¿POR QUÉ? (4)", blank=True, null=True)
    porque5_8 = models.TextField("¿POR QUÉ? (5)", blank=True, null=True)
    porque6_8 = models.TextField("¿POR QUÉ? (6)", blank=True, null=True)
    porque7_8 = models.TextField("¿POR QUÉ? (7)", blank=True, null=True)

    COLOR_CHOICES = [
        ('white', 'Blanco'),
        ('green', 'Verde'),
        ('red', 'Rojo'),
    ]

    
    color_validacion1 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion2 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion3 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion4 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion5 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion6 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion7 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')

    color_validacion1_2 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion2_2 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion3_2 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion4_2 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion5_2 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion6_2 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion7_2 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')

    color_validacion1_3 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion2_3 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion3_3 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion4_3 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion5_3 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion6_3 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion7_3 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')

    color_validacion1_4 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion2_4 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion3_4 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion4_4 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion5_4 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion6_4 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion7_4 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    
    color_validacion1_5 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion2_5 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion3_5 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion4_5 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion5_5 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion6_5 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion7_5 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')

    color_validacion1_6 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion2_6 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion3_6 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion4_6 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion5_6 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion6_6 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion7_6 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')

    color_validacion1_7 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion2_7 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion3_7 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion4_7 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion5_7 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion6_7 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion7_7 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')

    color_validacion1_8 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion2_8 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion3_8 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion4_8 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion5_8 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion6_8 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
    color_validacion7_8 = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')

    Raiz = models.TextField("Raíz", blank=True, null=True)
    Raiz_2 = models.TextField("Raíz", blank=True, null=True)
    Raiz_3 = models.TextField("Raíz", blank=True, null=True)
    Raiz_4 = models.TextField("Raíz", blank=True, null=True)
    Raiz_5 = models.TextField("Raíz", blank=True, null=True)
    Raiz_6 = models.TextField("Raíz", blank=True, null=True)
    Raiz_7 = models.TextField("Raíz", blank=True, null=True)
    Raiz_8 = models.TextField("Raíz", blank=True, null=True)

    M6 = [
            ('Máquina', 'Máquina'),
            ('Método', 'Método'),
            ('Medio Ambiente', 'Medio Ambiente'),
            ('Material', 'Material'),
            ('Medición', 'Medición'),
            ('Mano de Obra', 'Mano de Obra'),
  
        ]

    ISHIKAWA = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )

    ISHIKAWA_2 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_3 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_4 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_5 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_6 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_7 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_8 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    
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


class ImagenDeploy(models.Model):
    kaizen = models.ForeignKey(Kaizen, related_name='imagenes_deploy', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_deploy/')
    
    def __str__(self):
        return f"Imagen Deploy para {self.kaizen}"
    
class ImagenDescripcion(models.Model):
    kaizen = models.ForeignKey(Kaizen, related_name='imagenes_descripcion', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_descripcion/')
    
    def __str__(self):
        return f"Imagen Deploy para {self.kaizen}"

    

    
    
