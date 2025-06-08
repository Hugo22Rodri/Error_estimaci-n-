def estimacion_error_punto_fijo(g, x0, tol, max_iter=100):
    """
    Método de punto fijo con estimación iterativa del error.

    Args:
        g: Función de iteración (g(x)).
        x0: Valor inicial.
        tol: Tolerancia (criterio de parada).
        max_iter: Máximo de iteraciones.

    Returns:
        list: Historial de iteraciones con estimación de error.
        float: Solución aproximada.
        int: Número de iteraciones.
    """
    iteraciones = []
    x_prev = x0
    error_abs = float('inf')
    iter_count = 0
    
    for i in range(max_iter):
        x_act = g(x_prev)

        # Estimación del error
        if i > 0:
            error_abs = abs(x_act - x_prev)
            error_rel = error_abs / abs(x_act) if x_act != 0 else "∞"  # Evitar 'inf'
        else:
            error_abs = "∞"
            error_rel = "∞"

        # Guardar iteración
        iteraciones.append({
            'iteracion': i + 1,
            'x_prev': x_prev,
            'x_act': x_act,
            'error_abs': error_abs,
            'error_rel': error_rel,
            'error_porcentual': error_rel if isinstance(error_rel, str) else error_rel * 100
        })

        # Criterio de parada
        if isinstance(error_abs, float) and error_abs < tol:
            break

        x_prev = x_act
        iter_count = i + 1

    return iteraciones, x_act, iter_count
