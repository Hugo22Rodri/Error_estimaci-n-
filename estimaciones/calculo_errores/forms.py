from django import forms

class CalculoErroresForm(forms.Form):
    valor_real = forms.FloatField(
        label='Valor Real',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
        required=True
    )
    
    valor_aprox = forms.FloatField(
        label='Valor Aproximado',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
        required=True
    )