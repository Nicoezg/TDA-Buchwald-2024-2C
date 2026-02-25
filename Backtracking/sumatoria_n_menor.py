def max_sumatoria(lista, n):
    res = []
    return subset_sum(lista, 0, n, res, [])

def subset_sum(lista, indice, n, conjunto_actual, conjunto_maximo):
    if sum(conjunto_actual) == n:
        return conjunto_actual
    
    if indice == len(lista):
        if sum(conjunto_actual) > sum(conjunto_maximo):
            return conjunto_actual
        return conjunto_maximo
    
    elemento_actual = lista[indice]
    conjunto_actual.append(elemento_actual)
    if sum(conjunto_actual) <= n:
        conjunto_maximo = list(subset_sum(lista, indice + 1, n, conjunto_actual, conjunto_maximo))
    conjunto_actual.pop()
    if sum(conjunto_maximo) == n:
        return conjunto_maximo
    return subset_sum(lista, indice + 1, n, conjunto_actual, conjunto_maximo)
    



def _independent_set(grafo, vertices, actual, conjunto_actual, conjunto_maximo):
    if actual == len(grafo):
        if len(conjunto_actual) > len(conjunto_maximo):
            return set(conjunto_actual)
        return conjunto_maximo
    
    vertice_actual = vertices[actual]
    conjunto_actual.add(vertice_actual)
    if es_independent_set(grafo, conjunto_actual, vertice_actual):
        conjunto_maximo = _independent_set(grafo, vertices, actual + 1, conjunto_actual, conjunto_maximo)
    conjunto_actual.remove(vertice_actual)
    return _independent_set(grafo, vertices, actual + 1, conjunto_actual, conjunto_maximo)

def es_independent_set(grafo, conjunto, vertice_actual):
    for v in conjunto:
        if v == vertice_actual:
            continue
        if grafo.estan_unidos(v, vertice_actual):
            return False
    return True

print(max_sumatoria([1,2,3,4,5,6,8,9], 12))