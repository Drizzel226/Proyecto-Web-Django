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
            'tarjetas_atrasadas', 'lila_asociado', 'ejecuto_lila', 'mantenimiento_no_ejecutado', 'materiales_calidad',
            'modo_falla', 'imagen_falla', 'causas_raiz'
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
        }

    def __init__(self, *args, **kwargs):
        super(PorqueForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
