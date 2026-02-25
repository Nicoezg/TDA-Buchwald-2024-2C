from grafo import Grafo

def dominating_set_min(grafo):
    return list(_dominating_set_min(grafo, grafo.obtener_vertices(), 0, set(grafo.obtener_vertices()), set(grafo.obtener_vertices())))

def _dominating_set_min(grafo, vertices, actual, conjunto_actual, conjunto_minimo):
    if actual == len(grafo):
        if len(conjunto_actual) < len(conjunto_minimo):
            return set(conjunto_actual)
        return conjunto_minimo
    
    vertice_actual = vertices[actual]
    conjunto_actual.remove(vertice_actual)
    if es_dominating_set(grafo, conjunto_actual):
        conjunto_minimo = _dominating_set_min(grafo, vertices, actual + 1, conjunto_actual, conjunto_minimo)
    conjunto_actual.add(vertice_actual)
    return _dominating_set_min(grafo, vertices, actual + 1, conjunto_actual, conjunto_minimo)

def es_dominating_set(grafo, conjunto):
    for v in grafo:
        if v in conjunto:
            continue
        alguno_esta = False
        for w in grafo.adyacentes(v):
            if w in conjunto:
                alguno_esta = True
                break
        if not alguno_esta:
            return False
    return True
