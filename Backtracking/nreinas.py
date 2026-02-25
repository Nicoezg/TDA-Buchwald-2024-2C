from grafo import Grafo

def nreinas(n):
    grafo = construir_tablero(n)
    puestos = []
    vertices = list(grafo.obtener_vertices())
    _ubicacion_BT(grafo, vertices, 0, puestos, n)
    return puestos

def construir_tablero(n):
    casillero = lambda i, j: str(i + 1) +  str(j + 1)
    g = Grafo()
    for i in range(n):
        for j in range(n):
            g.agregar_vertice(casillero(i, j))

    # Agrego adyacencia por fila
    for i in range(n):
        for j in range(n):
            for k in range(j + 1, n):
                g.agregar_arista(casillero(i, j), casillero(i, k))
    # Agrego por columnas
    for j in range(n):
        for i in range(n):
            for k in range(i+1, n):
                g.agregar_arista(casillero(i, j), casillero(k, j))

    # agrego por diagonales
    for i in range(n):
        for j in range(n):
            for k in range(i):
                if k < j:
                    g.agregar_arista(casillero(i, j), casillero(i - k - 1, j - k - 1))
                if k + j + 1 < n:
                    g.agregar_arista(casillero(i, j), casillero(i - k - 1, j + k + 1))
    return g

def _ubicacion_BT(grafo, vertices, v_actual, puestos, n):
    if v_actual == len(grafo):
        return False
    if len(puestos) == n:
        return True

    # Mis opciones son poner acá, o no
    puestos.append(vertices[v_actual])
    if es_compatible(grafo, puestos, vertices[v_actual]) and _ubicacion_BT(grafo, vertices, v_actual + 1, puestos, n):
        return True
    puestos.pop()
    return _ubicacion_BT(grafo, vertices, v_actual + 1, puestos, n)

def es_compatible(grafo, puestos, ultimo_puesto):
    for w in puestos:
        if ultimo_puesto == w:
            continue
        if grafo.estan_unidos(ultimo_puesto, w):
            return False
    return True

print(nreinas(4))