from grafo import Grafo
from collections import deque

# O (E * V)

def grados_entrada(grafo):
    res = {}
    for v in grafo:
        if v not in res:
            res[v] = 0
        for w in grafo.adyacentes(v):
            if w not in res:
                res[w] = 0
            res[w] += 1
    return res

def perfect_bipartite_matching(grafo):
    grados_ent = grados_entrada(grafo)
    grafo.agregar_vertice('s')
    grafo.agregar_vertice('t')
    for v, g_e in grados_ent.items():
        if g_e == 0:
            grafo.agregar_arista('s', v, 1)
        else:
            grafo.agregar_arista(v, 't', 1)
    return flujo(grafo, 's', 't')




def obtener_camino(grafo,origen, destino): ##O (V + E)
   q = deque()
   visitados = set()
   orden = {origen : 0}
   q.append(origen)
   visitados.add(origen)
   padres = {origen: None}
   orden[origen] = 0

   while q:
      v = q.popleft()

      for w in grafo.adyacentes(v):
         if w not in visitados:
            q.append(w)
            visitados.add(w)
            if w not in orden or orden[w] > orden[v] + 1:
                padres[w] = v
                orden[w] = orden[v] + 1
   return reconstruir_camino(padres, origen, destino)

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


def flujo(grafo, s, t):
    flujo = {}
    for v in grafo:
        for w in grafo.adyacentes(v):
            flujo[(v, w)] = 0
    grafo_residual = copiar(grafo)
    camino = obtener_camino(grafo_residual, s, t)
    
    while camino:
        capacidad_residual_camino = min_peso(grafo_residual, camino)
        for i in range(1, len(camino)):
            if grafo.estan_unidos(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += capacidad_residual_camino
            else:
                flujo[(camino[i], camino[i-1])] -= capacidad_residual_camino
            actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual_camino)
        camino = obtener_camino(grafo_residual, s, t)

    return flujo

def actualizar_grafo_residual(grafo, v, w, capacidad_residual):
    peso_previo = grafo.peso_arista(v, w)
    grafo.borrar_arista(v, w)
    if peso_previo - capacidad_residual > 0:
        grafo.agregar_arista(v, w, peso_previo - capacidad_residual)
    if not grafo.estan_unidos(w, v):
        grafo.agregar_arista(w, v, capacidad_residual)
    elif grafo.estan_unidos(w, v):
        peso_previo = grafo.peso_arista(w, v)
        grafo.borrar_arista(w, v)
        grafo.agregar_arista(w, v, peso_previo + capacidad_residual)


def min_peso(grafo, camino):
    min_peso = float('inf')
    for i in range(1, len(camino)):
        if grafo.estan_unidos(camino[i-1], camino[i]):
            min_peso = min(min_peso, grafo.peso_arista(camino[i-1], camino[i]))
    return min_peso

def copiar(grafo):
    grafo_copia = Grafo(dirigido = True, pesado = True, vertices_iniciales=list(grafo.obtener_vertices()))
    for v in grafo:
        for w in grafo.adyacentes(v):
            grafo_copia.agregar_arista(v, w, grafo.peso_arista(v, w))
    return grafo_copia


grafo = Grafo(pesado=True, dirigido= True, vertices_iniciales=[2,4,6,8,10,1,3,5,7,9])
grafo.agregar_arista(2,1,1)
grafo.agregar_arista(2,5,1)
grafo.agregar_arista(4,1,1)
grafo.agregar_arista(4,3,1)
grafo.agregar_arista(4,5,1)
grafo.agregar_arista(4,7,1)
grafo.agregar_arista(6,7,1)
grafo.agregar_arista(8,7,1)
grafo.agregar_arista(10,7,1)
grafo.agregar_arista(10,9,1)
print(perfect_bipartite_matching(grafo))
