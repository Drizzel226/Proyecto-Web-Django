from django import forms
from .models import Porque, MiembroEquipo

class PorqueForm(forms.ModelForm):
    miembros_equipo = forms.ModelMultipleChoiceField(
        queryset=MiembroEquipo.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2'})
    )

    class Meta:
        model = Porque
        fields = [
            'categoria', 'subcategoria', 'area', 'subarea', 'maquina', 'miembros_equipo',
            'pilar', 'impacto', 'kpi_iceo', 'kpi_secundario', 'fecha_cierre',
            'que_ocurre', 'como_ocurre', 'donde_ocurre', 'cuando_ocurre', 'quien_presente',
            'senal_antes', 'descripcion_senal', 'falla_funcional', 'imagen_falla_funcional',
            'principio_funcionamiento', 'imagen_funcionamiento', 'condiciones_basicas',
            'tarjetas_atrasadas', 'lila_asociado', 'ejecuto_lila', 'mantenimiento_no_ejecutado',
            'materiales_calidad', 'modo_falla_paso2',

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

            # PASO 4

            'Accion_correctiva', 'Responsable1', 'Fecha_compromiso1', 'Accion_Preventiva', 'Responsable2', 'Fecha_compromiso2', 
        ]
        widgets = {
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategoria': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'subarea': forms.TextInput(attrs={'class': 'form-control'}),
            'maquina': forms.TextInput(attrs={'class': 'form-control'}),
            'pilar': forms.TextInput(attrs={'class': 'form-control'}),
            'impacto': forms.Textarea(attrs={'class': 'form-control'}),
            'kpi_iceo': forms.TextInput(attrs={'class': 'form-control'}),
            'kpi_secundario': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_cierre': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'que_ocurre': forms.Textarea(attrs={'class': 'form-control'}),
            'como_ocurre': forms.Textarea(attrs={'class': 'form-control'}),
            'donde_ocurre': forms.Textarea(attrs={'class': 'form-control'}),
            'cuando_ocurre': forms.Textarea(attrs={'class': 'form-control'}),
            'quien_presente': forms.Textarea(attrs={'class': 'form-control'}),
            'senal_antes': forms.Select(attrs={'class': 'form-control'}),
            'descripcion_senal': forms.Textarea(attrs={'class': 'form-control'}),
            'falla_funcional': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen_falla_funcional': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'principio_funcionamiento': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen_funcionamiento': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'condiciones_basicas': forms.Textarea(attrs={'class': 'form-control'}),
            
            'tarjetas_atrasadas': forms.RadioSelect(),
            'lila_asociado': forms.RadioSelect(),
            'ejecuto_lila': forms.RadioSelect(),
            'mantenimiento_no_ejecutado': forms.RadioSelect(),
            'materiales_calidad': forms.RadioSelect(),
            
            'modo_falla': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen_falla': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'modo_falla_paso2': forms.Textarea(attrs={'class': 'form-control'}),

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

            #paso 4
            'Accion_correctiva': forms.Textarea(attrs={'class': 'form-control'}),
            'Responsable1': forms.Textarea(attrs={'class': 'form-control'}),
            'Fecha_compromiso1': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Accion_Preventiva': forms.Textarea(attrs={'class': 'form-control'}),
            'Responsable2': forms.Textarea(attrs={'class': 'form-control'}),
            'Fecha_compromiso2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            



        }



    areas_aplicacion = forms.MultipleChoiceField(
        choices=[
            ('Linea 2', 'Línea 2'),
            ('Linea 3', 'Línea 3'),
            ('Linea 4', 'Línea 4'),
            ('Linea 9', 'Línea 9'),
            ('Linea 11', 'Línea 11'),
            ('Linea 12', 'Línea 12'),
            ('Linea 14', 'Línea 14'),
            ('Linea 15', 'Línea 15'),
            ('Taller de Mantenimiento', 'Taller de Mantenimiento'),
            ('Almacén de Repuestos', 'Almacén de Repuestos'),
            ('Elaboración', 'Elaboración'),
            ('Suministros', 'Suministros'),
            ('Almacén', 'Almacén'),
            ('Linea 7', 'Línea 7'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Si es opcional
    )











    def __init__(self, *args, **kwargs):
        super(PorqueForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
