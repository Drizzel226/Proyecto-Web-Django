from django import forms
from .models import Visu5Model

class Visu5ModelForm(forms.ModelForm):
     class Meta:
        model = Visu5Model
        fields = [
            'paso_4',
            ]
        
        widgets = {

        }