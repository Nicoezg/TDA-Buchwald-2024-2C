import pulp
from grafo import Grafo

def vertex_cover_min(grafo):
    y = []
    vertices = list(grafo.obtener_vertices())
    for i in range(len(vertices)):
        y.append(pulp.LpVariable("y" + str(i), cat="Binary"))
    
    problem = pulp.LpProblem("vertices", pulp.LpMinimize)
    for i in range(len(vertices)):
        for j in range (i + 1, len(vertices)):
            if grafo.estan_unidos(vertices[i],vertices[j]):
                problem += y[i] + y[j] >= 1
    problem += pulp.lpSum(y)
    problem.solve()
    res = []
    for i in range(len(vertices)):
        if pulp.value(y[i]) == 0:
            continue
        res.append(vertices[i])
    return res
    

grafo = Grafo(False, False, [1,2,3,4])
grafo.agregar_arista(3,4)
print(vertex_cover_min(grafo))