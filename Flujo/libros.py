from grafo import Grafo
from ford_fulkerson import obtener_camino, copiar, actualizar_grafo_residual, min_peso

def libros(grafo, s, t):
    flujo = {}
    for v in grafo:
        for w in grafo.adyacentes(v):
            flujo[(v,w)] = 0
    grafo_residual = copiar(grafo)
    camino = obtener_camino(grafo, s, t)
    
    while camino:
        min_p = min_peso(grafo_residual, camino)
        for i in range(1, len(camino)):
            if grafo.estan_unidos(camino[i - 1], camino[i]):
                flujo[(camino[i - 1], camino[i])] += min_p
            else:
                flujo[(camino[i], camino[i - 1])] -= min_p
            actualizar_grafo_residual(grafo_residual, camino[i - 1], camino[i], min_p)
        camino = obtener_camino(grafo_residual, s, t)
    return flujo


grafo = Grafo(dirigido = True, pesado = True, vertices_iniciales = ["S", "A", "B", "C", "1", "2", "3", "T"])
grafo.agregar_arista("S", "A", 10)
grafo.agregar_arista("S", "B", 10)
grafo.agregar_arista("S", "C", 10)
grafo.agregar_arista("A", "1", 1)
grafo.agregar_arista("A", "2", 1)
grafo.agregar_arista("A", "3", 1)
grafo.agregar_arista("3", "T", 3)
grafo.agregar_arista("2", "T", 3)
grafo.agregar_arista("1", "T", 3)
print(libros(grafo, "S", "T"))

