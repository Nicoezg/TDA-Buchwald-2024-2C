from grafo import Grafo

def vertex_cover(grafo):
    aristas = obtener_aristas(grafo)
    return list(_vertex_cover(grafo, list(grafo.obtener_vertices()), 0, set(grafo.obtener_vertices()), set(grafo.obtener_vertices()), aristas))

def _vertex_cover(grafo, vertices, actual, conjunto_actual, conjunto_minimo, aristas):
    if actual == len(grafo):
        if len(conjunto_actual) < len(conjunto_minimo):
            return set(conjunto_actual)
        return conjunto_minimo
    
    vertice_actual = vertices[actual]
    conjunto_actual.remove(vertice_actual)
    if es_vertex_cover(grafo, conjunto_actual, vertice_actual, aristas):
        conjunto_minimo = _vertex_cover(grafo, vertices, actual + 1, conjunto_actual, conjunto_minimo, aristas)
    conjunto_actual.add(vertice_actual)
    return _vertex_cover(grafo, vertices, actual + 1, conjunto_actual, conjunto_minimo, aristas)

def es_vertex_cover(grafo, conjunto, vertice_actual, aristas):
    for v, w in aristas:
        if not v in conjunto and not w in conjunto:
            return False
    return True 

def obtener_aristas(grafo):
    aristas = set()
    for v in grafo:
        for w in grafo.adyacentes(v):
            aristas.add((v, w))
    return aristas

            

grafo = Grafo(False, False, [1,2,3,4,5])
grafo.agregar_arista(1,2)
grafo.agregar_arista(1,3)
grafo.agregar_arista(1,4)
grafo.agregar_arista(4,5)
grafo.agregar_arista(3,5)
grafo.agregar_arista(2,5)
print(vertex_cover(grafo))
