from django import forms
from .models import Kaizen, MiembroEquipo

class KaizenForm(forms.ModelForm):
    miembros_equipo = forms.ModelMultipleChoiceField(
        queryset=MiembroEquipo.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2'})
    )
    genes_funcionamiento = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    imagenes_deploy = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    imagenes_descripcion = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    imagenes_definir = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    imagenes_estandar = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    imagenes_expansion = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Kaizen
        fields = [
            # Paso 0
            'Nombre_Kaizen', 'ahorro', 'categoria', 'subcategoria', 'area', 'subarea', 'maquina', 'miembros_equipo',
            'lider', 'pilar', 'meta', 'kpi_iceo', 'kpi_secundario','valor_inicial','valor_propuesto_final','valor_real_final', 'fecha_cierre',

            # Registor acciones generales
            'accion', 'observacion', 'Respon', 'opciones_acciones', 'ISHIKAWA_acciones', 'FechaCompr', 'FechaCierre_acciones',


            #Deployment de Perdida y Objetivo SMART
            'Deployment','especifico', 'medible', 'alcanzable', 'realista', 'tiempo',

            # Paso 1
            'descripcion', 'seleccion', 'imagen_falla_funcional',

            # Paso 2
            'condicion_basica', 'seleccion_paso2', 


            # Paso 3
            
            'desarrollo',

            'modo_falla_paso3',
            'porque1', 'color_validacion1',
            'porque2', 'color_validacion2',
            'porque3', 'color_validacion3',
            'porque4', 'color_validacion4',
            'porque5', 'color_validacion5',
            'porque6', 'color_validacion6',
            'porque7', 'color_validacion7',

            'modo_falla_paso3_2',
            'porque1_2', 'color_validacion1_2',
            'porque2_2', 'color_validacion2_2',
            'porque3_2', 'color_validacion3_2',
            'porque4_2', 'color_validacion4_2',
            'porque5_2', 'color_validacion5_2',
            'porque6_2', 'color_validacion6_2',
            'porque7_2', 'color_validacion7_2',

            'modo_falla_paso3_3',
            'porque1_3', 'color_validacion1_3',
            'porque2_3', 'color_validacion2_3',
            'porque3_3', 'color_validacion3_3',
            'porque4_3', 'color_validacion4_3',
            'porque5_3', 'color_validacion5_3',
            'porque6_3', 'color_validacion6_3',
            'porque7_3', 'color_validacion7_3',

            'modo_falla_paso3_4',
            'porque1_4', 'color_validacion1_4',
            'porque2_4', 'color_validacion2_4',
            'porque3_4', 'color_validacion3_4',
            'porque4_4', 'color_validacion4_4',
            'porque5_4', 'color_validacion5_4',
            'porque6_4', 'color_validacion6_4',
            'porque7_4', 'color_validacion7_4',

            'modo_falla_paso3_5',
            'porque1_5', 'color_validacion1_5',
            'porque2_5', 'color_validacion2_5',
            'porque3_5', 'color_validacion3_5',
            'porque4_5', 'color_validacion4_5',
            'porque5_5', 'color_validacion5_5',
            'porque6_5', 'color_validacion6_5',
            'porque7_5', 'color_validacion7_5',

            'modo_falla_paso3_6',
            'porque1_6', 'color_validacion1_6',
            'porque2_6', 'color_validacion2_6',
            'porque3_6', 'color_validacion3_6',
            'porque4_6', 'color_validacion4_6',
            'porque5_6', 'color_validacion5_6',
            'porque6_6', 'color_validacion6_6',
            'porque7_6', 'color_validacion7_6',

            'modo_falla_paso3_7',
            'porque1_7', 'color_validacion1_7',
            'porque2_7', 'color_validacion2_7',
            'porque3_7', 'color_validacion3_7',
            'porque4_7', 'color_validacion4_7',
            'porque5_7', 'color_validacion5_7',
            'porque6_7', 'color_validacion6_7',
            'porque7_7', 'color_validacion7_7',

            'modo_falla_paso3_8',
            'porque1_8', 'color_validacion1_8',
            'porque2_8', 'color_validacion2_8',
            'porque3_8', 'color_validacion3_8',
            'porque4_8', 'color_validacion4_8',
            'porque5_8', 'color_validacion5_8',
            'porque6_8', 'color_validacion6_8',
            'porque7_8', 'color_validacion7_8',

            'Raiz',
            'Raiz_2',
            'Raiz_3',
            'Raiz_4',
            'Raiz_5',
            'Raiz_6',
            'Raiz_7',
            'Raiz_8',

            'ISHIKAWA',
            'ISHIKAWA_2',
            'ISHIKAWA_3',
            'ISHIKAWA_4',
            'ISHIKAWA_5',
            'ISHIKAWA_6',
            'ISHIKAWA_7',
            'ISHIKAWA_8',
        

            # PASO 4
            'seleccion_paso4',

            'Accion_Preventiva', 'Responsable2', 'Fecha_inicio2', 'Fecha_compromiso2',  'estado',
            'Fecha_cierre_paso4', 

            'Accion_Preventiva_2', 'Responsable2_2', 'Fecha_inicio2_2', 'Fecha_compromiso2_2', 'estado_2',
            'Fecha_cierre_paso4_2', 

            'Accion_Preventiva_3', 'Responsable2_3', 'Fecha_inicio2_3', 'Fecha_compromiso2_3', 'estado_3',
            'Fecha_cierre_paso4_3', 

            'Accion_Preventiva_4', 'Responsable2_4', 'Fecha_inicio2_4', 'Fecha_compromiso2_4', 'estado_4',
            'Fecha_cierre_paso4_4', 

            'Accion_Preventiva_5', 'Responsable2_5', 'Fecha_inicio2_5', 'Fecha_compromiso2_5', 'estado_5', 'Fecha_cierre_paso4_5',
            'Accion_Preventiva_6', 'Responsable2_6', 'Fecha_inicio2_6', 'Fecha_compromiso2_6', 'estado_6', 'Fecha_cierre_paso4_6',
            'Accion_Preventiva_7', 'Responsable2_7', 'Fecha_inicio2_7', 'Fecha_compromiso2_7', 'estado_7', 'Fecha_cierre_paso4_7',
            'Accion_Preventiva_8', 'Responsable2_8', 'Fecha_inicio2_8', 'Fecha_compromiso2_8', 'estado_8', 'Fecha_cierre_paso4_8',
            'Accion_Preventiva_9', 'Responsable2_9', 'Fecha_inicio2_9', 'Fecha_compromiso2_9', 'estado_9', 'Fecha_cierre_paso4_9',
            'Accion_Preventiva_10', 'Responsable2_10', 'Fecha_inicio2_10', 'Fecha_compromiso2_10', 'estado_10', 'Fecha_cierre_paso4_10',

            
            #PASO 5
            'seleccion_paso5',

            'estandarizacion_TA',
            'Estandarizacion', 'Responsable3', 'Fecha_compromiso3',
            'Estandarizacion_2', 'Responsable3_2', 'Fecha_compromiso3_2',
            'Estandarizacion_3', 'Responsable3_3', 'Fecha_compromiso3_3',
            'Estandarizacion_4', 'Responsable3_4', 'Fecha_compromiso3_4',


            'expansion_TA',
            'Expansion', 'Responsable4', 'Fecha_compromiso4',
            'Expansion_2', 'Responsable4_2', 'Fecha_compromiso4_2',
            'Expansion_3', 'Responsable4_3', 'Fecha_compromiso4_3',
            'Expansion_4', 'Responsable4_4', 'Fecha_compromiso4_4',

            'puntaje'

        ]
        widgets = {
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategoria': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'subarea': forms.TextInput(attrs={'class': 'form-control'}),
            'maquina': forms.TextInput(attrs={'class': 'form-control'}),
            'pilar': forms.TextInput(attrs={'class': 'form-control'}),
            'meta': forms.Textarea(attrs={'class': 'form-control'}),
            'kpi_iceo': forms.TextInput(attrs={'class': 'form-control'}),
            'kpi_secundario': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_inicial': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_propuesto_final': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_real_final': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_cierre': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            # Registor acciones generales
            #'Respon', 'ISHIKAWA_acciones', 'FechaCompr', 'FechaCierre_acciones',

            'accion': forms.Textarea(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),

            'opciones_acciones': forms.RadioSelect(),
            'ISHIKAWA_acciones': forms.RadioSelect(),
            'FechaCompr': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'FechaCierre_acciones': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
            # Deployment de Perdida y Objetivo SMART

            'Deployment': forms.Textarea(attrs={'class': 'form-control'}),
            'especifico': forms.Textarea(attrs={'class': 'form-control'}),
            'medible': forms.Textarea(attrs={'class': 'form-control'}),
            'alcanzable': forms.Textarea(attrs={'class': 'form-control'}),
            'realista': forms.Textarea(attrs={'class': 'form-control'}),
            'tiempo': forms.Textarea(attrs={'class': 'form-control'}),

            # Paso 1
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'seleccion': forms.RadioSelect(),
            

            # Paso 2
            'condicion_basica': forms.Textarea(attrs={'class': 'form-control'}),
            'seleccion_paso2': forms.RadioSelect(),
            

            # Paso 3

            'desarrollo': forms.Textarea(attrs={'class': 'form-control'}),

            'modo_falla_paso3': forms.Textarea(attrs={'class': 'form-control'}),
            'porque1': forms.Textarea(attrs={'class': 'form-control'}),
            'porque2': forms.Textarea(attrs={'class': 'form-control'}),
            'porque3': forms.Textarea(attrs={'class': 'form-control'}),
            'porque4': forms.Textarea(attrs={'class': 'form-control'}),
            'porque5': forms.Textarea(attrs={'class': 'form-control'}),
            'porque6': forms.Textarea(attrs={'class': 'form-control'}),
            'porque7': forms.Textarea(attrs={'class': 'form-control'}),

            'modo_falla_paso3_2': forms.Textarea(attrs={'class': 'form-control'}),
            'porque1_2': forms.Textarea(attrs={'class': 'form-control'}),
            'porque2_2': forms.Textarea(attrs={'class': 'form-control'}),
            'porque3_2': forms.Textarea(attrs={'class': 'form-control'}),
            'porque4_2': forms.Textarea(attrs={'class': 'form-control'}),
            'porque5_2': forms.Textarea(attrs={'class': 'form-control'}),
            'porque6_2': forms.Textarea(attrs={'class': 'form-control'}),
            'porque7_2': forms.Textarea(attrs={'class': 'form-control'}),

            'modo_falla_paso3_3': forms.Textarea(attrs={'class': 'form-control'}),
            'porque1_3': forms.Textarea(attrs={'class': 'form-control'}),
            'porque2_3': forms.Textarea(attrs={'class': 'form-control'}),
            'porque3_3': forms.Textarea(attrs={'class': 'form-control'}),
            'porque4_3': forms.Textarea(attrs={'class': 'form-control'}),
            'porque5_3': forms.Textarea(attrs={'class': 'form-control'}),
            'porque6_3': forms.Textarea(attrs={'class': 'form-control'}),
            'porque7_3': forms.Textarea(attrs={'class': 'form-control'}),

            'modo_falla_paso3_4': forms.Textarea(attrs={'class': 'form-control'}),
            'porque1_4': forms.Textarea(attrs={'class': 'form-control'}),
            'porque2_4': forms.Textarea(attrs={'class': 'form-control'}),
            'porque3_4': forms.Textarea(attrs={'class': 'form-control'}),
            'porque4_4': forms.Textarea(attrs={'class': 'form-control'}),
            'porque5_4': forms.Textarea(attrs={'class': 'form-control'}),
            'porque6_4': forms.Textarea(attrs={'class': 'form-control'}),
            'porque7_4': forms.Textarea(attrs={'class': 'form-control'}),

            'modo_falla_paso3_5': forms.Textarea(attrs={'class': 'form-control'}),
            'porque1_5': forms.Textarea(attrs={'class': 'form-control'}),
            'porque2_5': forms.Textarea(attrs={'class': 'form-control'}),
            'porque3_5': forms.Textarea(attrs={'class': 'form-control'}),
            'porque4_5': forms.Textarea(attrs={'class': 'form-control'}),
            'porque5_5': forms.Textarea(attrs={'class': 'form-control'}),
            'porque6_5': forms.Textarea(attrs={'class': 'form-control'}),
            'porque7_5': forms.Textarea(attrs={'class': 'form-control'}),

            'modo_falla_paso3_6': forms.Textarea(attrs={'class': 'form-control'}),
            'porque1_6': forms.Textarea(attrs={'class': 'form-control'}),
            'porque2_6': forms.Textarea(attrs={'class': 'form-control'}),
            'porque3_6': forms.Textarea(attrs={'class': 'form-control'}),
            'porque4_6': forms.Textarea(attrs={'class': 'form-control'}),
            'porque5_6': forms.Textarea(attrs={'class': 'form-control'}),
            'porque6_6': forms.Textarea(attrs={'class': 'form-control'}),
            'porque7_6': forms.Textarea(attrs={'class': 'form-control'}),

            'modo_falla_paso3_7': forms.Textarea(attrs={'class': 'form-control'}),
            'porque1_7': forms.Textarea(attrs={'class': 'form-control'}),
            'porque2_7': forms.Textarea(attrs={'class': 'form-control'}),
            'porque3_7': forms.Textarea(attrs={'class': 'form-control'}),
            'porque4_7': forms.Textarea(attrs={'class': 'form-control'}),
            'porque5_7': forms.Textarea(attrs={'class': 'form-control'}),
            'porque6_7': forms.Textarea(attrs={'class': 'form-control'}),
            'porque7_7': forms.Textarea(attrs={'class': 'form-control'}),

            'modo_falla_paso3_8': forms.Textarea(attrs={'class': 'form-control'}),
            'porque1_8': forms.Textarea(attrs={'class': 'form-control'}),
            'porque2_8': forms.Textarea(attrs={'class': 'form-control'}),
            'porque3_8': forms.Textarea(attrs={'class': 'form-control'}),
            'porque4_8': forms.Textarea(attrs={'class': 'form-control'}),
            'porque5_8': forms.Textarea(attrs={'class': 'form-control'}),
            'porque6_8': forms.Textarea(attrs={'class': 'form-control'}),
            'porque7_8': forms.Textarea(attrs={'class': 'form-control'}),


            'color_validacion1': forms.HiddenInput(),
            'color_validacion2': forms.HiddenInput(),
            'color_validacion3': forms.HiddenInput(),
            'color_validacion4': forms.HiddenInput(),
            'color_validacion5': forms.HiddenInput(),
            'color_validacion6': forms.HiddenInput(),
            'color_validacion7': forms.HiddenInput(),

            'color_validacion1_2': forms.HiddenInput(),
            'color_validacion2_2': forms.HiddenInput(),
            'color_validacion3_2': forms.HiddenInput(),
            'color_validacion4_2': forms.HiddenInput(),
            'color_validacion5_2': forms.HiddenInput(),
            'color_validacion6_2': forms.HiddenInput(),
            'color_validacion7_2': forms.HiddenInput(),

            'color_validacion1_3': forms.HiddenInput(),
            'color_validacion2_3': forms.HiddenInput(),
            'color_validacion3_3': forms.HiddenInput(),
            'color_validacion4_3': forms.HiddenInput(),
            'color_validacion5_3': forms.HiddenInput(),
            'color_validacion6_3': forms.HiddenInput(),
            'color_validacion7_3': forms.HiddenInput(),

            'color_validacion1_4': forms.HiddenInput(),
            'color_validacion2_4': forms.HiddenInput(),
            'color_validacion3_4': forms.HiddenInput(),
            'color_validacion4_4': forms.HiddenInput(),
            'color_validacion5_4': forms.HiddenInput(),
            'color_validacion6_4': forms.HiddenInput(),
            'color_validacion7_4': forms.HiddenInput(),

            'color_validacion1_5': forms.HiddenInput(),
            'color_validacion2_5': forms.HiddenInput(),
            'color_validacion3_5': forms.HiddenInput(),
            'color_validacion4_5': forms.HiddenInput(),
            'color_validacion5_5': forms.HiddenInput(),
            'color_validacion6_5': forms.HiddenInput(),
            'color_validacion7_5': forms.HiddenInput(),

            'color_validacion1_6': forms.HiddenInput(),
            'color_validacion2_6': forms.HiddenInput(),
            'color_validacion3_6': forms.HiddenInput(),
            'color_validacion4_6': forms.HiddenInput(),
            'color_validacion5_6': forms.HiddenInput(),
            'color_validacion6_6': forms.HiddenInput(),
            'color_validacion7_6': forms.HiddenInput(),

            'color_validacion1_7': forms.HiddenInput(),
            'color_validacion2_7': forms.HiddenInput(),
            'color_validacion3_7': forms.HiddenInput(),
            'color_validacion4_7': forms.HiddenInput(),
            'color_validacion5_7': forms.HiddenInput(),
            'color_validacion6_7': forms.HiddenInput(),
            'color_validacion7_7': forms.HiddenInput(),

            'color_validacion1_8': forms.HiddenInput(),
            'color_validacion2_8': forms.HiddenInput(),
            'color_validacion3_8': forms.HiddenInput(),
            'color_validacion4_8': forms.HiddenInput(),
            'color_validacion5_8': forms.HiddenInput(),
            'color_validacion6_8': forms.HiddenInput(),
            'color_validacion7_8': forms.HiddenInput(),

            'Raiz': forms.Textarea(attrs={'class': 'form-control'}),
            'Raiz_2': forms.Textarea(attrs={'class': 'form-control'}),
            'Raiz_3': forms.Textarea(attrs={'class': 'form-control'}),
            'Raiz_4': forms.Textarea(attrs={'class': 'form-control'}),
            'Raiz_5': forms.Textarea(attrs={'class': 'form-control'}),
            'Raiz_6': forms.Textarea(attrs={'class': 'form-control'}),
            'Raiz_7': forms.Textarea(attrs={'class': 'form-control'}),
            'Raiz_8': forms.Textarea(attrs={'class': 'form-control'}),

            'ISHIKAWA': forms.Select(attrs={'class': 'form-control'}),
            'ISHIKAWA_2': forms.Select(attrs={'class': 'form-control'}),
            'ISHIKAWA_3': forms.Select(attrs={'class': 'form-control'}),
            'ISHIKAWA_4': forms.Select(attrs={'class': 'form-control'}),
            'ISHIKAWA_5': forms.Select(attrs={'class': 'form-control'}),
            'ISHIKAWA_6': forms.Select(attrs={'class': 'form-control'}),
            'ISHIKAWA_7': forms.Select(attrs={'class': 'form-control'}),
            'ISHIKAWA_8': forms.Select(attrs={'class': 'form-control'}),

            # Paso 4

            'seleccion_paso4': forms.RadioSelect(),

            'Accion_Preventiva': forms.Textarea(attrs={'class': 'accion-correctiva'}),
            'Accion_Preventiva_2': forms.Textarea(attrs={'class': 'accion-correctiva'}),
            'Accion_Preventiva_3': forms.Textarea(attrs={'class': 'accion-correctiva'}),
            'Accion_Preventiva_4': forms.Textarea(attrs={'class': 'accion-correctiva'}),
            'Accion_Preventiva_5': forms.Textarea(attrs={'class': 'accion-correctiva'}),
            'Accion_Preventiva_6': forms.Textarea(attrs={'class': 'accion-correctiva'}),
            'Accion_Preventiva_7': forms.Textarea(attrs={'class': 'accion-correctiva'}),
            'Accion_Preventiva_8': forms.Textarea(attrs={'class': 'accion-correctiva'}),
            'Accion_Preventiva_9': forms.Textarea(attrs={'class': 'accion-correctiva'}),
            'Accion_Preventiva_10': forms.Textarea(attrs={'class': 'accion-correctiva'}),

            'Fecha_inicio2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_inicio2_2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_inicio2_3': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_inicio2_4': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_inicio2_5': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_inicio2_6': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_inicio2_7': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_inicio2_8': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_inicio2_9': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_inicio2_10': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'Fecha_compromiso2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_compromiso2_2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_compromiso2_3': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_compromiso2_4': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_compromiso2_5': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_compromiso2_6': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_compromiso2_7': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_compromiso2_8': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_compromiso2_9': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_compromiso2_10': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'Fecha_cierre_paso4': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_cierre_paso4_2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_cierre_paso4_3': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_cierre_paso4_4': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_cierre_paso4_5': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_cierre_paso4_6': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_cierre_paso4_7': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_cierre_paso4_8': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_cierre_paso4_9': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_cierre_paso4_10': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),


    # Paso 5
            'seleccion_paso5': forms.RadioSelect(),

            'estandarizacion_TA': forms.Textarea(attrs={'class': 'form-control'}),

            'Estandarizacion': forms.Textarea(attrs={'class': 'accion-correctiva'}), 
            'Fecha_compromiso3': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),

            'Estandarizacion_2': forms.Textarea(attrs={'class': 'accion-correctiva'}), 
            'Fecha_compromiso3_2': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),

            'Estandarizacion_3': forms.Textarea(attrs={'class': 'accion-correctiva'}), 
            'Fecha_compromiso3_3': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),

            'Estandarizacion_4': forms.Textarea(attrs={'class': 'accion-correctiva'}), 
            'Fecha_compromiso3_4': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),



            'expansion_TA': forms.Textarea(attrs={'class': 'form-control'}),

            'Expansion': forms.Textarea(attrs={'class': 'accion-correctiva'}), 
            'Fecha_compromiso4': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),

            'Expansion_2': forms.Textarea(attrs={'class': 'accion-correctiva'}), 
            'Fecha_compromiso4_2': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),

            'Expansion_3': forms.Textarea(attrs={'class': 'accion-correctiva'}), 
            'Fecha_compromiso4_3': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),

            'Expansion_4': forms.Textarea(attrs={'class': 'accion-correctiva'}), 
            'Fecha_compromiso4_4': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),

        }




    areas_aplicacion = forms.MultipleChoiceField(
        choices=[
            ('Linea 3', 'Línea 3'),
            ('Linea 4', 'Línea 4'),
            ('Linea 5', 'Línea 5'),
            ('Linea 6', 'Línea 6'),
            ('Taller de Mantenimiento', 'Taller de Mantenimiento'),
            ('Almacén de Repuestos', 'Almacén de Repuestos'),
            ('Elaboración', 'Elaboración'),
            ('Suministros', 'Suministros'),
            ('Almacén', 'Almacén'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Si es opcional
    )









    def __init__(self, *args, **kwargs):
        super(KaizenForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = False
