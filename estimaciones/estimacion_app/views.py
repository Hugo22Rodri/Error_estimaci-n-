from django.shortcuts import render
from .forms import IterationForm
from .utils import procesar_iteraciones

def index(request):
    resultados = None
    if request.method == 'POST':
        form = IterationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['iterations']
            valores = []
            for item in data.replace(',', ' ').split():
                try:
                    valores.append(float(item.strip()))
                except ValueError:
                    pass
            
            if len(valores) < 2:
                form.add_error('iterations', 'Se requieren al menos 2 valores')
            else:
                resultados = procesar_iteraciones(valores)
    else:
        form = IterationForm()
    
    return render(request, 'estimacion_app/index.html', {
        'form': form,
        'resultados': resultados
    })