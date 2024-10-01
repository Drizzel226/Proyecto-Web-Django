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

            'Raiz',
            'Raiz_2',
            'Raiz_3',
            'Raiz_4',
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

            'Raiz': forms.Textarea(attrs={'class': 'form-control'}),
            'Raiz_2': forms.Textarea(attrs={'class': 'form-control'}),
            'Raiz_3': forms.Textarea(attrs={'class': 'form-control'}),
            'Raiz_4': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PorqueForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
