def sumatoria_dados(n, s):
    res = []
    if s / n > 6:
        return res
    return _sumatoria_rec(n, s, res)


def _sumatoria_rec(n, s, solucion_parcial):
    if len(solucion_parcial) == n:
        return [solucion_parcial]
    if not solucion_posible(solucion_parcial, s, n):
        return []
    
    soluciones = []
    for cara in range(1,7):
        if solucion_posible(solucion_parcial, s - cara, n - 1):
            soluciones += _sumatoria_rec(n, s, solucion_parcial + [cara])
    return soluciones

def solucion_posible(solucion_parcial, s, n):
    if n - len(solucion_parcial) > s:
        return False
    if sum(solucion_parcial) > s:
        return False
    if (n - len(solucion_parcial)) * 6 < s -  sum(solucion_parcial):
        return False
    return True

print(sumatoria_dados(2,7))