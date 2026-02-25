""" 
Problema de decision: el problema de decisión será si existe un
set de (al menos) tamaño k. Queremos que el problema sea booleano.
"""

def verificador_independent_set(grafo, conjunto, k):
    if len(conjunto) < k: # O(1)
        return False
    for vertice in conjunto: # O(V)
        if vertice not in grafo:
            return False
    
    for vertice in conjunto: #O(V + E)
        for adyacente in grafo.adyacentes(vertice):
            if adyacente in conjunto:
                return False
    return True

