from grafo import Grafo
from collections import deque
from reconstruccion import reconstruir_red_residual

def augmenting_path(grafo_residual, s, t):
    visitados = set()
    cola = deque()
    cola.append(s)
    visitados.add(s)
    padres = {s: None}

    while cola:
        v = cola.popleft()
        if v == t:
            break
        for w in grafo_residual.adyacentes(v):
            if w not in visitados:
                cola.append(w)
                visitados.add(w)
                padres[w] = v

    return reconstruir_camino(padres, s, t)

def reconstruir_camino(padres, origen, destino):
    camino = []
    actual = destino
    while actual != None:
            camino.append(actual)
            if actual == origen:
                    break
            if actual not in padres:
                return None
            actual = padres[actual]
    return camino[::-1]

grafo = Grafo(dirigido = True, pesado = True, vertices_iniciales = [0,1,2,3,4,5])
grafo.agregar_arista(0, 1, 11)
grafo.agregar_arista(0, 2, 12)
grafo.agregar_arista(2, 1, 2)
grafo.agregar_arista(2, 4, 11)
grafo.agregar_arista(1, 3, 12)
grafo.agregar_arista(4, 3, 10)
grafo.agregar_arista(3, 5, 19)
grafo.agregar_arista(4, 5, 4)
print(augmenting_path(grafo, 0, 5))

