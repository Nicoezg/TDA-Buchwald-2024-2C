from grafo import Grafo

def independent_set(grafo):
    return list(_independent_set(grafo, list(grafo.obtener_vertices()), 0, set(), set()))

def _independent_set(grafo, vertices, actual, conjunto_actual, conjunto_maximo):
    if actual == len(grafo):
        if len(conjunto_actual) > len(conjunto_maximo):
            return set(conjunto_actual)
        return conjunto_maximo
    
    vertice_actual = vertices[actual]
    conjunto_actual.add(vertice_actual)
    if es_independent_set(grafo, conjunto_actual, vertice_actual):
        conjunto_maximo = _independent_set(grafo, vertices, actual + 1, conjunto_actual, conjunto_maximo)
    conjunto_actual.remove(vertice_actual)
    return _independent_set(grafo, vertices, actual + 1, conjunto_actual, conjunto_maximo)

def es_independent_set(grafo, conjunto, vertice_actual):
    for v in conjunto:
        if v == vertice_actual:
            continue
        if grafo.estan_unidos(v, vertice_actual):
            return False
    return True

grafo = Grafo(False, False, [1,2,3,4,5])
grafo.agregar_arista(1,2)
grafo.agregar_arista(1,3)
grafo.agregar_arista(1,4)
grafo.agregar_arista(4,5)
grafo.agregar_arista(3,5)
grafo.agregar_arista(2,5)
print(independent_set(grafo))
