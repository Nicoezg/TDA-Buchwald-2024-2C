from grafo import Grafo

def colorear(grafo, n):
    vertices = list(grafo.obtener_vertices())
    colores = {}
    return _coloreo_rec(grafo, n, vertices, 0, colores)
        


def _coloreo_rec(grafo, k, vertices, indice_actual, colores):
    if indice_actual == len(grafo):
        return True
    
    v_actual = vertices[indice_actual]
    for color in range(k):
        colores[v_actual] = color
        if not colores or es_coloreo_compatible(grafo, colores, v_actual):
            if _coloreo_rec(grafo, k, vertices, indice_actual + 1, colores):
                return True
    del colores[v_actual]
    return False

def es_coloreo_compatible(grafo, colores, ultimo):
    for v in grafo.adyacentes(ultimo):
        if v in colores:
            if colores[v] == colores[ultimo]:
                return False
    return True

grafo = Grafo(False, False, [1,2,3])
grafo.agregar_arista(1,2)
grafo.agregar_arista(2,3)
grafo.agregar_arista(3,1)
print(colorear(grafo, 2))