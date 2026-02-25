from grafo import Grafo
def cant_combinaciones(grafo, pasos, tecla_inicial):
    cant = []
    nueva_fila = []
    for j in range(10):
        nueva_fila.append(1)
    cant.append(nueva_fila)
    for i in range(1, pasos):
        nueva_fila = []
        for tecla in range(10):
            contador = 0
            for vecino in grafo.adyacentes(tecla):
                contador += cant[i - 1][vecino]
            nueva_fila.append(contador + cant[i - 1][tecla])
        cant.append(nueva_fila)
    return cant[pasos - 1][tecla_inicial]

def crear_grafo():
    grafo = Grafo(False, False, [0,1,2,3,4,5,6,7,8,9])
    grafo.agregar_arista(0, 8)
    grafo.agregar_arista(8, 5)
    grafo.agregar_arista(8, 9)
    grafo.agregar_arista(8, 7)
    grafo.agregar_arista(7, 4)
    grafo.agregar_arista(9, 6)
    grafo.agregar_arista(5, 4)
    grafo.agregar_arista(5, 6)
    grafo.agregar_arista(5, 2)
    grafo.agregar_arista(4, 1)
    grafo.agregar_arista(6, 3)
    grafo.agregar_arista(2, 3)
    grafo.agregar_arista(2, 1)
    return grafo

print(cant_combinaciones(crear_grafo(), 2, 0))
