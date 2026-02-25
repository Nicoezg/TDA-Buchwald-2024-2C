import pulp
from grafo import Grafo

def dominating_set(grafo):
    y = []
    vertices = list(grafo.obtener_vertices())
    for i in range(len(vertices)):
        y.append(pulp.LpVariable("y" + str(i), cat="Binary"))
    pintados = set()
    
    problem = pulp.LpProblem("vertices", pulp.LpMinimize)
    for i in range(len(vertices)):
        for j in range (i + 1, len(vertices)):
            if grafo.estan_unidos(vertices[i],vertices[j]) and vertices[j] not in pintados:
                pintados.add(vertices[j])
                problem += y[i] + y[j] >= 1
    problem += pulp.lpSum(y)
    problem.solve()
    return list(map(lambda yi: pulp.value(yi), y))
    

grafo = Grafo(False, False, [1,2,3,4,5,6])
grafo.agregar_arista(1,2)
grafo.agregar_arista(1,3)
grafo.agregar_arista(1,4)
grafo.agregar_arista(1,5)
grafo.agregar_arista(1,6)

print(dominating_set(grafo))