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

    # Paso 1
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

    # Paso 2
    principio_funcionamiento = models.TextField("Comprender el principio de funcionamiento de la máquina o proceso, incluyendo estándares y parámetros de trabajo", blank=True, null=True)
    imagen_funcionamiento = models.ImageField(upload_to='imagenes_funcionamiento/', blank=True, null=True)
    condiciones_basicas = models.TextField("Verificar condiciones básicas definidas e identificar desviaciones que impacten en el problema", blank=True, null=True)

    RESPUESTA_CHOICES = [
        ('no', 'NO'),
        ('no_aplica', 'NO APLICA'),
        ('si', 'SI'),
    ]

    tarjetas_atrasadas = models.CharField(
        "¿Hay tarjetas atrasadas o pendientes asociadas a la falla funcional?",
        max_length=10,
        choices=RESPUESTA_CHOICES,
        default='no_aplica',
        blank=False,
        null=True
    )

    lila_asociado = models.CharField(
        "¿Hay LILA asociado a la máquina?",
        max_length=10,
        choices=RESPUESTA_CHOICES,
        default='no_aplica',
        blank=False,
        null=True
    )

    ejecuto_lila = models.CharField(
        "¿Se ejecutó correctamente el LILA?",
        max_length=10,
        choices=RESPUESTA_CHOICES,
        default='no_aplica',
        blank=False,
        null=True
    )

    mantenimiento_no_ejecutado = models.CharField(
        "¿Hay actividades de mantenimiento no ejecutadas asociadas a la falla funcional (revisar plan de 52 semanas)?",
        max_length=10,
        choices=RESPUESTA_CHOICES,
        default='no_aplica',
        blank=False,
        null=True
    )

    materiales_calidad = models.CharField(
        "¿Los materiales cumplen con las especificaciones de calidad?",
        max_length=10,
        choices=RESPUESTA_CHOICES,
        default='no_aplica',
        blank=False,
        null=True
    )

    modo_falla_paso2 = models.TextField("El modo de falla corresponde al evento o situación que causa la falla funcional. Ej: presión inestable por válvula rota, inspector detecta elemento extraño pero no lo rechaza, inspector no detecta elemento extraño, sulfatación de sensor de seguridad, etc.", blank=True, null=True)
    imagen_falla = models.ImageField(upload_to='imagenes_falla/', blank=True, null=True)


    # PASO 3

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
