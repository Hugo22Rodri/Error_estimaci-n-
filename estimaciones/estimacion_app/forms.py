from django import forms

class IterationForm(forms.Form):
    iterations = forms.CharField(
        label='Valores de Iteración',
        widget=forms.Textarea(attrs={
            'rows': 5,
            'placeholder': 'Ingrese valores separados por comas o espacios\nEjemplo: 5, 3.2, 2.5, 2.1'
        }),
        help_text='Ingrese los valores de cada iteración en orden'
    )