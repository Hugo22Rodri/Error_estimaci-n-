def calcular_error_aproximado(valor_actual, valor_anterior):
    """Calcula el error aproximado porcentual"""
    if valor_actual == 0:
        return 0.0
    return abs((valor_actual - valor_anterior) / valor_actual) * 100

def procesar_iteraciones(iteraciones):
    """Procesa la lista de iteraciones y calcula los errores"""
    resultados = []
    for i, valor in enumerate(iteraciones):
        if i == 0:
            error = None
        else:
            error = calcular_error_aproximado(valor, iteraciones[i-1])
        resultados.append({
            'iteracion': i,
            'valor': valor,
            'error': error
        })
    return resultados