from grafo import Grafo

def no_adyacentes(grafo, n):
    'Devolver una lista con los n vértices, o None de no ser posible'
    res = []
    visitados = set()
    for v in grafo:
        if _no_adyacentes(grafo, n, visitados, res, v):
            return res
    return None

def _no_adyacentes(grafo, n, visitados, res, v):
    visitados.add(v)
    res.append(v)
    if len(res) == n:
        return True
    for w in grafo:
        if es_compatible(grafo, w, res) and w not in visitados:
            if _no_adyacentes(grafo, n, visitados, res, w):
                return True
    visitados.remove(v)
    res.pop()
    return False

def es_compatible(grafo, s, res):
    for vertice in res:
        if grafo.estan_unidos(vertice, s):
            return False
    return True

grafo = Grafo(False, False, [1,2,3,4])
print(no_adyacentes(grafo, 4))