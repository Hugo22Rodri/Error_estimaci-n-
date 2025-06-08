from django.shortcuts import render
import math

from estimaciones.calculo_errores.utils import estimacion_error_punto_fijo

def metodo_estimacion_error(request):
    context = {}
    
    if request.method == 'POST':
        try:
            # Obtener parámetros del formulario
            funcion = request.POST.get('funcion')
            x0 = float(request.POST.get('x0'))
            tol = float(request.POST.get('tolerancia'))
            
            # Definir función g(x)
            def g(x):
                return eval(funcion, {'__builtins__': None}, {'x': x, 'math': math, 'e': math.e, 'pi': math.pi})
            
            # Ejecutar método de estimación de error
            iteraciones, solucion, num_iter = estimacion_error_punto_fijo(g, x0, tol)
            
            context = {
                'funcion': funcion,
                'x0': x0,
                'tol': tol,
                'iteraciones': iteraciones,
                'solucion': solucion,
                'num_iter': num_iter,
                'convergio': num_iter < 100
            }
            
        except Exception as e:
            context['error'] = f"Error en los datos: {str(e)}"
    
    return render(request, 'calculo_errores/estimacion_error.html', context)