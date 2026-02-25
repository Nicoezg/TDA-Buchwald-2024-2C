"""
Problema de decisión: Plantear si existe un set de tamaño (al menos) k.
"""

def verificador_vertex_cover(grafo, conjunto, k):
    if len(conjunto) < k: # O(1)
        return False
    for vertice in conjunto: # O(V)
        if vertice not in conjunto:
            return False
    aristas = obtener_aristas(grafo) # O(E)
    for v, w in aristas: # O (E)
        if not v in conjunto and not w in conjunto:
            return False
    return True
