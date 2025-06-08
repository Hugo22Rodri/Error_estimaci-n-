def error_absoluto(valor_real, valor_aproximado):
    try:
        return abs(float(valor_real) - float(valor_aproximado))
    except (ValueError, TypeError):
        return None

def error_relativo(valor_real, valor_aproximado):
    try:
        vr = float(valor_real)
        va = float(valor_aproximado)
        if vr == 0:
            return float('inf')
        return abs((vr - va) / vr)
    except (ValueError, TypeError):
        return None

def error_relativo_porcentual(valor_real, valor_aproximado):
    error_rel = error_relativo(valor_real, valor_aproximado)
    if error_rel is None:
        return None
    if error_rel == float('inf'):
        return float('inf')
    return error_rel * 100