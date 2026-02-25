from grafo import Grafo

def independent_set(grafo):
    res = []
    visitados = set()
    for v in grafo:
        if _independent_set(grafo, visitados, res, v):
            return res
    print(res)
    return None

def _independent_set(grafo, visitados, res, v):
    visitados.add(v)
    res.append(v)
    for w in grafo:
        if es_compatible(grafo, w, res) and w not in visitados:
            _independent_set(grafo, visitados, res, res, w)
            
    visitados.remove(v)
    res.pop()
    return res

def es_compatible(grafo, s, res):
    for vertice in res:
        if grafo.estan_unidos(vertice, s):
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