from django.shortcuts import render
from .forms import CalculoErroresForm

def calcular_errores(valor_real, valor_aprox):
    """
    Calcula el error absoluto, relativo y porcentual entre un valor real y uno aproximado.
    
    Args:
        valor_real (float): Valor considerado como real o exacto.
        valor_aprox (float): Valor aproximado o medido.
        
    Returns:
        tuple: Una tupla con tres valores: 
            - error_abs (float): Error absoluto
            - error_rel (float): Error relativo
            - error_porc (float): Error porcentual
    """
    error_abs = abs(valor_real - valor_aprox)
    
    # Manejar el caso especial cuando el valor real es cero
    if valor_real == 0:
        error_rel = float('inf') if valor_aprox != 0 else 0.0
    else:
        error_rel = error_abs / abs(valor_real)
    
    error_porc = error_rel * 100
    return error_abs, error_rel, error_porc

def calcular_errores_view(request):
    # Inicializar variables
    resultados = None
    form = CalculoErroresForm()
    
    if request.method == 'POST':
        form = CalculoErroresForm(request.POST)
        if form.is_valid():
            valor_real = form.cleaned_data['valor_real']
            valor_aprox = form.cleaned_data['valor_aprox']
            
            # Calcular errores
            error_abs, error_rel, error_porc = calcular_errores(valor_real, valor_aprox)
            
            # Formatear resultados para mostrar
            resultados = {
                'valor_real': valor_real,
                'valor_aprox': valor_aprox,
                'error_abs': f"{error_abs:.6f}",
                'error_rel': f"{error_rel:.6f}" if error_rel != float('inf') else "infinito",
                'error_porc': f"{error_porc:.4f}%" if error_porc != float('inf') else "infinito%",
            }
            
            # Renderizar la página de resultados
            return render(request, 'calculo_errores/resultados.html', {
                'resultados': resultados,
                'form': form  # Mantener el formulario para nuevo cálculo
            })
    
    # Renderizar el formulario (GET o POST con errores)
    return render(request, 'calculo_errores/calcular_errores.html', {
        'form': form,
        'resultados': resultados
    })