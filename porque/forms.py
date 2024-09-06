from django import forms
from .models import Porque, Paso2, Paso3, Paso4, Paso5

class PorqueForm(forms.ModelForm):
    class Meta:
        model = Porque
        fields = ['nombre', 'email', 'asunto', 'mensaje', 'categoria', 'prioridad', 'seguimiento']
        
        
class Paso2Form(forms.ModelForm):
    class Meta:
        model = Paso2
        fields = ['campo_1', 'campo2', 'campo3']

class Paso3Form(forms.ModelForm):
    class Meta:
        model = Paso3
        fields = ['campo1', 'campo2', 'campo3']

class Paso4Form(forms.ModelForm):
    class Meta:
        model = Paso4
        fields = ['campo1', 'campo2', 'campo3']

class Paso5Form(forms.ModelForm):
    class Meta:
        model = Paso5
        fields = ['campo1', 'campo2', 'campo3']
