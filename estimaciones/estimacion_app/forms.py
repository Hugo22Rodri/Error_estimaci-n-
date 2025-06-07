from django import forms
from .models import Estimacion

class EstimacionForm(forms.ModelForm):
    class Meta:
        model = Estimacion
        fields = ['muestras', 'nivel_confianza']
