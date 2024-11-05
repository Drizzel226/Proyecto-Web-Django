from django import forms
from .models import VisuMiniModel

class Visu5ModelForm(forms.ModelForm):
     class Meta:
        model = VisuMiniModel
        fields = [
            'paso_4',
            ]
        
        widgets = {

        }