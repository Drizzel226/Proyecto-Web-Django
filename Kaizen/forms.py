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

    class Meta:
        model = Kaizen
        fields = [
            # Paso 0
            'Nombre_Kaizen', 'ahorro', 'categoria', 'subcategoria', 'area', 'subarea', 'maquina', 'miembros_equipo',
            'lider', 'pilar', 'meta', 'kpi_iceo', 'kpi_secundario','valor_inicial','valor_propuesto_final','valor_real_final', 'fecha_cierre',

            #Deployment de Perdida y Objetivo SMART
            'Deployment','especifico', 'medible', 'alcanzable', 'realista', 'tiempo',

            # Paso 1
            'descripcion', 'imagen_falla_funcional',

            # Paso 2
            'condicion_basica', 'imagen_funcionamiento', 


            # Paso 3
            'ISHIKAWA',
            'desarrollo',
        

            # PASO 4

            'Accion_Preventiva', 'Responsable2', 'Fecha_inicio2', 'Fecha_compromiso2',  'estado',
            'Fecha_cierre_paso4', 

            'Accion_Preventiva_2', 'Responsable2_2', 'Fecha_inicio2_2', 'Fecha_compromiso2_2', 'estado_2',
            'Fecha_cierre_paso4_2', 

            'Accion_Preventiva_3', 'Responsable2_3', 'Fecha_inicio2_3', 'Fecha_compromiso2_3', 'estado_3',
            'Fecha_cierre_paso4_3', 

            'Accion_Preventiva_4', 'Responsable2_4', 'Fecha_inicio2_4', 'Fecha_compromiso2_4', 'estado_4',
            'Fecha_cierre_paso4_4', 
            
            #PASO 5

            'Estandarizacion', 'Responsable3', 'Fecha_compromiso3',
            'Estandarizacion_2', 'Responsable3_2', 'Fecha_compromiso3_2',
            'Estandarizacion_3', 'Responsable3_3', 'Fecha_compromiso3_3',
            'Estandarizacion_4', 'Responsable3_4', 'Fecha_compromiso3_4',

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

            # Deployment de Perdida y Objetivo SMART

            'Deployment': forms.Textarea(attrs={'class': 'form-control'}),
            'especifico': forms.Textarea(attrs={'class': 'form-control'}),
            'medible': forms.Textarea(attrs={'class': 'form-control'}),
            'alcanzable': forms.Textarea(attrs={'class': 'form-control'}),
            'realista': forms.Textarea(attrs={'class': 'form-control'}),
            'tiempo': forms.Textarea(attrs={'class': 'form-control'}),

            # Paso 1
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            

            # Paso 2
            'condicion_basica': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen_funcionamiento': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            
            

            # Paso 3

            'ISHIKAWA': forms.Select(attrs={'class': 'form-control'}),
            'desarrollo': forms.Textarea(attrs={'class': 'form-control'}),

            

            # Paso 4

            'Accion_Preventiva': forms.Textarea(attrs={'class': 'accion-correctiva'}),
            'Accion_Preventiva_2': forms.Textarea(attrs={'class': 'accion-correctiva'}),
            'Accion_Preventiva_3': forms.Textarea(attrs={'class': 'accion-correctiva'}),
            'Accion_Preventiva_4': forms.Textarea(attrs={'class': 'accion-correctiva'}),

            'Fecha_inicio2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_inicio2_2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_inicio2_3': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_inicio2_4': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'Fecha_compromiso2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_compromiso2_2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_compromiso2_3': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_compromiso2_4': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'Fecha_cierre_paso4': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_cierre_paso4_2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_cierre_paso4_3': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_cierre_paso4_4': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),


    # Paso 5

            'Estandarizacion': forms.Textarea(attrs={'class': 'accion-correctiva'}), 
            'Fecha_compromiso3': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),

            'Estandarizacion_2': forms.Textarea(attrs={'class': 'accion-correctiva'}), 
            'Fecha_compromiso3_2': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),

            'Estandarizacion_3': forms.Textarea(attrs={'class': 'accion-correctiva'}), 
            'Fecha_compromiso3_3': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),

            'Estandarizacion_4': forms.Textarea(attrs={'class': 'accion-correctiva'}), 
            'Fecha_compromiso3_4': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),



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
