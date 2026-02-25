""" Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta en una unidad la capacidad 
a una artista (por ejemplo, a una arista de capacidad 3 se le aumenta a 4, permita obtener el nuevo flujo máximo en tiempo 
lineal en vértices y aristas. Indicar y justificar la complejidad del algoritmo implementado. """

from grafo import Grafo
from augmenting_path import augmenting_path

def flujo_max(flujo, grafo_residual):
    camino = augmenting_path(grafo_residual)
    if not camino:
        return flujo
    for i in range(1, len(camino)):
        if grafo_residual.estan_unidos(camino[i-1], camino[i]):
            flujo[(camino[i-1], camino[i])] += 1
        else:
            flujo[(camino[i], camino[i-1])] -= 1





ejemplo = {(0, 1): 11, (0, 2): 12, (1, 3): 12, (2, 1): 1, (2, 4): 11, (3, 5): 19, (4, 3): 7, (4, 5): 4}