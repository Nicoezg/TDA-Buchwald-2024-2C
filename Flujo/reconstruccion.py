from grafo import Grafo

def reconstruir_red_residual(dicc, grafo):
    grafo_residual = Grafo(dirigido=True, pesado=True, vertices_iniciales=list(grafo.obtener_vertices()))
    for arista, peso in dicc.items():
        peso_original = grafo.peso_arista(arista[0], arista[1])
        if peso_original != peso:
            grafo_residual.agregar_arista(arista[0], arista[1], peso_original - peso)
        grafo_residual.agregar_arista(arista[1], arista[0], peso)
    return grafo_residual




ejemplo = {(0, 1): 11, (0, 2): 12, (1, 3): 12, (2, 1): 1, (2, 4): 11, (3, 5): 19, (4, 3): 7, (4, 5): 4}
grafo = Grafo(dirigido = True, pesado = True, vertices_iniciales = [0,1,2,3,4,5])
grafo.agregar_arista(0, 1, 11)
grafo.agregar_arista(0, 2, 12)
grafo.agregar_arista(2, 1, 2)
grafo.agregar_arista(2, 4, 11)
grafo.agregar_arista(1, 3, 12)
grafo.agregar_arista(4, 3, 10)
grafo.agregar_arista(3, 5, 19)
grafo.agregar_arista(4, 5, 4)
print(reconstruir_red_residual(ejemplo, grafo))