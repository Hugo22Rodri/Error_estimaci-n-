from django.shortcuts import render
from .models import Estimacion
from .forms import EstimacionForm
import numpy as np
import matplotlib.pyplot as plt

def calcular_estimacion(request):
    form = EstimacionForm(request.POST or None)

    if form.is_valid():
        muestras = form.cleaned_data['muestras']
        nivel_confianza = form.cleaned_data['nivel_confianza']
        error = 1 / np.sqrt(muestras)

        estimacion = Estimacion.objects.create(
            muestras=muestras,
            error_estimacion=error,
            nivel_confianza=nivel_confianza
        )

        # Generar gráfico
        plt.figure()
        plt.plot(np.linspace(10, 200, 10), 1 / np.sqrt(np.linspace(10, 200, 10)), marker='o')
        plt.xlabel('Número de muestras')
        plt.ylabel('Error estimado')
        plt.title('Error de estimación')
        plt.savefig('estimacion/static/grafico.png')

    estimaciones = Estimacion.objects.all()
    return render(request, 'estimacion/index.html', {'form': form, 'estimaciones': estimaciones})
