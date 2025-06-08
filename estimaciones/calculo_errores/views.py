from django.shortcuts import render
from .utils import error_absoluto, error_relativo, error_relativo_porcentual

def calcular_errores(request):
    return render(request, 'calculo_errores/calcular_errores.html')

def resultados(request):
    context = {}
    resultado = None
    tipo_error = None
    
    if request.method == 'POST':
        valor_real = request.POST.get('valor_real')
        valor_aprox = request.POST.get('valor_aprox')
        tipo_error = request.POST.get('tipo_error')
        
        if tipo_error == 'absoluto':
            resultado = error_absoluto(valor_real, valor_aprox)
        elif tipo_error == 'relativo':
            resultado = error_relativo(valor_real, valor_aprox)
        elif tipo_error == 'porcentual':
            resultado = error_relativo_porcentual(valor_real, valor_aprox)
        
        if resultado == float('inf'):
            resultado = "∞"  # Representar infinito como un símbolo seguro para la plantilla

        context = {
            'valor_real': valor_real,
            'valor_aprox': valor_aprox,
            'resultado': resultado,
            'tipo_error': tipo_error
        }
    
    return render(request, 'calculo_errores/resultados.html', context)