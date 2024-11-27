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

    # Registor acciones generales

    acc = [
            ('accion imediata (correccion)', 'Acción imediata (corrección)'),
            ('accion orientada causa raiz (correctiva)', 'Acción orientada causa raíz (correctiva)'),
            ('accion preventiva', 'Acción preventiva'),
  
        ]
    
    M6 = [
            ('Máquina', 'Máquina'),
            ('Método', 'Método'),
            ('Medio Ambiente', 'Medio Ambiente'),
            ('Material', 'Material'),
            ('Medición', 'Medición'),
            ('Mano de Obra', 'Mano de Obra'),
  
        ]
    
    ESTADO_OPCIONES = [
    ('Pendiente', 'Pendiente'),
    ('Cerrada', 'Cerrada'),
    ]
    
    accion = models.TextField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    Respon = models.ManyToManyField('MiembroEquipo', related_name="respon", blank=True)
    opciones_acciones = models.CharField(
        max_length=100,
        choices=acc,
        blank=True, null=True
    )
    
    ISHIKAWA_acciones = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    FechaInicio_acciones = models.DateField(blank=True, null=True)
    FechaCompr = models.DateField(blank=True, null=True)
    estado_accion = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    FechaCierre_acciones = models.DateField(blank=True, null=True)


    accion_2 = models.TextField(blank=True, null=True)
    observacion_2 = models.TextField(blank=True, null=True)
    Respon_2 = models.ManyToManyField('MiembroEquipo', related_name="respon_2", blank=True)
    opciones_acciones_2 = models.CharField(
        max_length=100,
        choices=acc,
        blank=True, null=True
    )
    ISHIKAWA_acciones_2 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    FechaInicio_acciones_2 = models.DateField(blank=True, null=True)
    FechaCompr_2 = models.DateField(blank=True, null=True)
    estado_accion_2 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    FechaCierre_acciones_2 = models.DateField(blank=True, null=True)

    accion_3 = models.TextField(blank=True, null=True)
    accion_4 = models.TextField(blank=True, null=True)
    accion_5 = models.TextField(blank=True, null=True)
    accion_6 = models.TextField(blank=True, null=True)
    accion_7 = models.TextField(blank=True, null=True)
    accion_8 = models.TextField(blank=True, null=True)
    accion_9 = models.TextField(blank=True, null=True)
    accion_10 = models.TextField(blank=True, null=True)

    observacion_3 = models.TextField(blank=True, null=True)
    observacion_4 = models.TextField(blank=True, null=True)
    observacion_5 = models.TextField(blank=True, null=True)
    observacion_6 = models.TextField(blank=True, null=True)
    observacion_7 = models.TextField(blank=True, null=True)
    observacion_8 = models.TextField(blank=True, null=True)
    observacion_9 = models.TextField(blank=True, null=True)
    observacion_10 = models.TextField(blank=True, null=True)

    Respon_3 = models.ManyToManyField('MiembroEquipo', related_name="respon_3", blank=True)
    Respon_4 = models.ManyToManyField('MiembroEquipo', related_name="respon_4", blank=True)
    Respon_5 = models.ManyToManyField('MiembroEquipo', related_name="respon_5", blank=True)
    Respon_6 = models.ManyToManyField('MiembroEquipo', related_name="respon_6", blank=True)
    Respon_7 = models.ManyToManyField('MiembroEquipo', related_name="respon_7", blank=True)
    Respon_8 = models.ManyToManyField('MiembroEquipo', related_name="respon_8", blank=True)
    Respon_9 = models.ManyToManyField('MiembroEquipo', related_name="respon_9", blank=True)
    Respon_10 = models.ManyToManyField('MiembroEquipo', related_name="respon_10", blank=True)

    opciones_acciones_3 = models.CharField(
        max_length=100,
        choices=acc,
        blank=True, null=True
    )
    opciones_acciones_4 = models.CharField(
        max_length=100,
        choices=acc,
        blank=True, null=True
    )
    opciones_acciones_5 = models.CharField(
        max_length=100,
        choices=acc,
        blank=True, null=True
    )
    opciones_acciones_6 = models.CharField(
        max_length=100,
        choices=acc,
        blank=True, null=True
    )
    opciones_acciones_7 = models.CharField(
        max_length=100,
        choices=acc,
        blank=True, null=True
    )
    opciones_acciones_8 = models.CharField(
        max_length=100,
        choices=acc,
        blank=True, null=True
    )
    opciones_acciones_9 = models.CharField(
        max_length=100,
        choices=acc,
        blank=True, null=True
    )
    opciones_acciones_10 = models.CharField(
        max_length=100,
        choices=acc,
        blank=True, null=True
    )

    ISHIKAWA_acciones_3 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_acciones_4 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_acciones_5 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_acciones_6 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_acciones_7 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_acciones_8 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_acciones_9 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )
    ISHIKAWA_acciones_10 = models.CharField(
        max_length=100,
        choices=M6,
        blank=True, null=True
    )

    FechaInicio_acciones_3 = models.DateField(blank=True, null=True)
    FechaInicio_acciones_4 = models.DateField(blank=True, null=True)
    FechaInicio_acciones_5 = models.DateField(blank=True, null=True)
    FechaInicio_acciones_6 = models.DateField(blank=True, null=True)
    FechaInicio_acciones_7 = models.DateField(blank=True, null=True)
    FechaInicio_acciones_8 = models.DateField(blank=True, null=True)
    FechaInicio_acciones_9 = models.DateField(blank=True, null=True)
    FechaInicio_acciones_10 = models.DateField(blank=True, null=True)

    FechaCompr_3 = models.DateField(blank=True, null=True)
    FechaCompr_4 = models.DateField(blank=True, null=True)
    FechaCompr_5 = models.DateField(blank=True, null=True)
    FechaCompr_6 = models.DateField(blank=True, null=True)
    FechaCompr_7 = models.DateField(blank=True, null=True)
    FechaCompr_8 = models.DateField(blank=True, null=True)
    FechaCompr_9 = models.DateField(blank=True, null=True)
    FechaCompr_10 = models.DateField(blank=True, null=True)

    estado_accion_3 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_accion_4 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_accion_5 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_accion_6 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_accion_7 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_accion_8 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_accion_9 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_accion_10 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')

    FechaCierre_acciones_3 = models.DateField(blank=True, null=True)
    FechaCierre_acciones_4 = models.DateField(blank=True, null=True)
    FechaCierre_acciones_5 = models.DateField(blank=True, null=True)
    FechaCierre_acciones_6 = models.DateField(blank=True, null=True)
    FechaCierre_acciones_7 = models.DateField(blank=True, null=True)
    FechaCierre_acciones_8 = models.DateField(blank=True, null=True)
    FechaCierre_acciones_9 = models.DateField(blank=True, null=True)
    FechaCierre_acciones_10 = models.DateField(blank=True, null=True)





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

    
    seleccion_paso4 = models.CharField(
        "Selección:",
        max_length=30,
        choices=[
                ('moc', 'MOC'),
                ('otros, especificar', 'Otros, especificar'),
            ],
        default='no_aplica',
        blank=False,
        null=True
    )


    Accion_Preventiva = models.TextField(blank=True, null=True)
    Accion_Preventiva_2 = models.TextField(blank=True, null=True)
    Accion_Preventiva_3 = models.TextField(blank=True, null=True)
    Accion_Preventiva_4 = models.TextField(blank=True, null=True)
    Accion_Preventiva_5 = models.TextField(blank=True, null=True)
    Accion_Preventiva_6 = models.TextField(blank=True, null=True)
    Accion_Preventiva_7 = models.TextField(blank=True, null=True)
    Accion_Preventiva_8 = models.TextField(blank=True, null=True)
    Accion_Preventiva_9 = models.TextField(blank=True, null=True)
    Accion_Preventiva_10 = models.TextField(blank=True, null=True)

    Responsable2 = models.ManyToManyField('MiembroEquipo', related_name="responsable2", blank=True)
    Responsable2_2 = models.ManyToManyField('MiembroEquipo', related_name="responsable2_2", blank=True)
    Responsable2_3 = models.ManyToManyField('MiembroEquipo', related_name="responsable2_3", blank=True)
    Responsable2_4 = models.ManyToManyField('MiembroEquipo', related_name="responsable2_4", blank=True)
    Responsable2_5 = models.ManyToManyField('MiembroEquipo', related_name="responsable2_5", blank=True)
    Responsable2_6 = models.ManyToManyField('MiembroEquipo', related_name="responsable2_6", blank=True)
    Responsable2_7 = models.ManyToManyField('MiembroEquipo', related_name="responsable2_7", blank=True)
    Responsable2_8 = models.ManyToManyField('MiembroEquipo', related_name="responsable2_8", blank=True)
    Responsable2_9 = models.ManyToManyField('MiembroEquipo', related_name="responsable2_9", blank=True)
    Responsable2_10 = models.ManyToManyField('MiembroEquipo', related_name="responsable2_10", blank=True)

    Fecha_inicio2 = models.DateField(blank=True, null=True)
    Fecha_inicio2_2 = models.DateField(blank=True, null=True)
    Fecha_inicio2_3 = models.DateField(blank=True, null=True)
    Fecha_inicio2_4 = models.DateField(blank=True, null=True)
    Fecha_inicio2_5 = models.DateField(blank=True, null=True)
    Fecha_inicio2_6 = models.DateField(blank=True, null=True)
    Fecha_inicio2_7 = models.DateField(blank=True, null=True)
    Fecha_inicio2_8 = models.DateField(blank=True, null=True)
    Fecha_inicio2_9 = models.DateField(blank=True, null=True)
    Fecha_inicio2_10 = models.DateField(blank=True, null=True)

    Fecha_compromiso2 = models.DateField(blank=True, null=True)
    Fecha_compromiso2_2 = models.DateField(blank=True, null=True)
    Fecha_compromiso2_3 = models.DateField(blank=True, null=True)
    Fecha_compromiso2_4 = models.DateField(blank=True, null=True)
    Fecha_compromiso2_5 = models.DateField(blank=True, null=True)
    Fecha_compromiso2_6 = models.DateField(blank=True, null=True)
    Fecha_compromiso2_7 = models.DateField(blank=True, null=True)
    Fecha_compromiso2_8 = models.DateField(blank=True, null=True)
    Fecha_compromiso2_9 = models.DateField(blank=True, null=True)
    Fecha_compromiso2_10 = models.DateField(blank=True, null=True)

    
    estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_2 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_3 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_4 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_5 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_6 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_7 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_8 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_9 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    estado_10 = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')

    Fecha_cierre_paso4 = models.DateField(blank=True, null=True)
    Fecha_cierre_paso4_2 = models.DateField(blank=True, null=True)
    Fecha_cierre_paso4_3 = models.DateField(blank=True, null=True)
    Fecha_cierre_paso4_4 = models.DateField(blank=True, null=True)
    Fecha_cierre_paso4_5 = models.DateField(blank=True, null=True)
    Fecha_cierre_paso4_6 = models.DateField(blank=True, null=True)
    Fecha_cierre_paso4_7 = models.DateField(blank=True, null=True)
    Fecha_cierre_paso4_8 = models.DateField(blank=True, null=True)
    Fecha_cierre_paso4_9 = models.DateField(blank=True, null=True)
    Fecha_cierre_paso4_10 = models.DateField(blank=True, null=True)
    



    # PASO 5

    seleccion_paso5 = models.CharField(
        "Selección:",
        max_length=30,
        choices=[
                ('estándar nuevo LUP', 'Estándar nuevo LUP'),
                ('poka yoke', 'Poka Yoke'),
                ('gestión visual', 'Gestión Visual'),
                ('disparador', 'Disparador'),
            ],
        default='no_aplica',
        blank=False,
        null=True
    )

    estandarizacion_TA = models.TextField("Estandarización de perdidas", blank=True, null=True)

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



    expansion_TA = models.TextField("Expansión de perdidas", blank=True, null=True)

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
        return f"Imagen Descripcion para {self.kaizen}"
    
class ImagenDefinir(models.Model):
    kaizen = models.ForeignKey(Kaizen, related_name='imagenes_definir', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_definir/')
    
    def __str__(self):
        return f"Imagen Definir para {self.kaizen}"

class ImagenEstandar(models.Model):
    kaizen = models.ForeignKey(Kaizen, related_name='imagenes_estandar', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_estandar/')
    
    def __str__(self):
        return f"Imagen Estandar para {self.kaizen}"
    
class ImagenExpansion(models.Model):
    kaizen = models.ForeignKey(Kaizen, related_name='imagenes_expansion', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_expansion/')
    
    def __str__(self):
        return f"Imagen Expansion para {self.kaizen}"

    
    
