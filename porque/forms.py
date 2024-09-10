from django import forms
from .models import Porque, Paso2


class PorqueForm(forms.ModelForm):
    class Meta:
        model = Porque
        fields = ['area', 'subarea', 'maquina', 'miembros_equipo', 'pilar', 
            'impacto', 'kpi_iceo', 'kpi_secundario', 'fecha_inicio', 'fecha_cierre']

    def clean(self):
        cleaned_data = super().clean()
        # Aquí puedes añadir validaciones adicionales si es necesario
        return cleaned_data


        
class Paso2Form(forms.ModelForm):
    class Meta:
        model = Paso2
        fields = ['campo_1', 'campo2', 'campo3']

