from django import forms
from .models import Porque, MiembroEquipo, Paso1


from django import forms
from .models import Porque, MiembroEquipo

class PorqueForm(forms.ModelForm):
    miembros_equipo = forms.ModelMultipleChoiceField(
        queryset=MiembroEquipo.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2'})
    )

    class Meta:
        model = Porque
        fields = ['categoria','subcategoria', 'area', 'subarea', 'maquina', 'miembros_equipo', 'pilar', 
                  'impacto', 'kpi_iceo', 'kpi_secundario', 'fecha_inicio', 'fecha_cierre']



    def clean(self):
        cleaned_data = super().clean()
        # Aquí puedes añadir validaciones adicionales si es necesario
        return cleaned_data



from django import forms
from .models import Paso1

class Paso1Form(forms.ModelForm):
    class Meta:
        model = Paso1
        fields = [
            'descripcion_problema', 
            'donde_ocurre', 
            'como_ocurre', 
            'cuando_ocurre', 
            'quien_presente', 
            'senal_antes', 
            'descripcion_senal',
            'falla_funcional',  # Campo nuevo
            'imagen_falla_funcional',  # Campo nuevo
        ]
        widgets = {
            'descripcion_problema': forms.Textarea(attrs={'class': 'form-control'}),
            'donde_ocurre': forms.Textarea(attrs={'class': 'form-control'}),
            'como_ocurre': forms.Textarea(attrs={'class': 'form-control'}),
            'cuando_ocurre': forms.Textarea(attrs={'class': 'form-control'}),
            'quien_presente': forms.Textarea(attrs={'class': 'form-control'}),
            'senal_antes': forms.Select(attrs={'class': 'form-control'}),
            'descripcion_senal': forms.Textarea(attrs={'class': 'form-control'}),
            'falla_funcional': forms.Textarea(attrs={'class': 'form-control'}),  # Widget del nuevo campo
            'imagen_falla_funcional': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # Widget del nuevo campo
        }
