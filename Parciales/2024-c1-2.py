from grafo import Grafo
"""
Definimos a un grafo ordenado como un grafo dirigido con vértices v1, · · · , vn en el que todos los vértices, salvo vn
tienen al menos una arista que sale del vértice, y cada arista va de un vértice de menor índice a uno de mayor índice (es
decir, las aristas tienen la forma (vi, vj ) con i < j). Implementar un algoritmo de programación dinámica que dado
un grafo ordenado (y, si les resulta útil, una lista con los vértices en orden) determine cuál es la longitud del camino más
largo. Dar la ecuación de recurrencia correspondiente. Dar también el algoritmo de recontrucción de la solución. Indicar
y justificar la complejidad del algoritmo implementado. Se pone a continuación un ejemplo de un grafo ordenado.
"""
def camino_mas_largo(grafo, vertices):
    res = {}
    # O(V + E), por cada vértice vemos sus adyacentes.
    for i in range(len(vertices)- 1, -1, - 1):
        res[vertices[i]] = 0
        for w in grafo.adyacentes(vertices[i]):
            if res[w] + 1 > res[vertices[i]]:
                res[vertices[i]] = res[w] + 1
    return reconstruir_camino(grafo, res)

def reconstruir_camino(grafo, res):
    max = 0
    vertice = None
    # O(V), recorremos cada vértice del grafo
    for v, d in res.items():
        if d > max:
            max = d
            vertice = v
    # O(V + E) a lo sumo recorremos cada vértice y todos sus adyacentes.
    camino = []
    while vertice != None:
        camino.append(vertice)
        for w in grafo.adyacentes(vertice):
            if res[w] == 0:
                camino.append(w)
                return camino
            if res[w] == res[vertice] - 1:
                vertice = w
                break
    return camino

"""
La complejidad del algoritmo es O(V + E), siendo V la cantidad de vértices en el grafo camino y E la cantidad de aristas en
el mismo.

OPT(Vi) = max(OPT(adyacentes(Vi))) + 1

Donde Vi es el vértice i en el grafo o lista de vértices. Entre todos los óptimos de los adyacentes a Vi, nos quedamos con
el de mayor valor y le sumamos 1. De esta manera, los vértices en el diccionario contendrán el máximo camino posible empezando
por ahí.
"""


"""
2) La Cruz Roja cuenta con n ambulancias, de las cuáles conoce la ubicación de cada una. En un momento dado llegan
p pedidos de ambulancias para socorrer personas. Debido a diferentes reglas que tienen, una ambulancia no debe
trasladarse más de k kilómetros. Se quiere saber si se puede hacer una asignación de ambulancias a los pedidos,
asignando cada una a como máximo 1 pedido. Implementar un algoritmo que resuelva este problema, utilizando redes
de flujo. Indicar y justificar la complejidad del algoritmo implementado para el problema planteado.
"""

def cruz_roja(ambulancias, pedidos, k):
    grafo = Grafo(True, True)
    grafo.agregar_vertice("fuente")
    grafo.agregar_vertice("sumidero")
    for ambulancia in ambulancias:
        grafo.agregar_vertice(ambulancia)
        grafo.agregar_arista("fuente", ambulancia, 1)
    
    for paciente, distancia in pedidos:
        grafo.agregar_vertice(paciente)
        grafo.agregar_arista(paciente, "sumidero", 1)
    
    for ambulancia in ambulancias:
        for paciente, distancia in pedidos:
            if distancia < k:
                grafo.agregar_arista(ambulancia, paciente, 1)

    res = flujo(grafo, "fuente", "sumidero")
    suma = res["sumidero"]
    return len(pedidos) == suma


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

"""Implementar un algoritmo greedy que permita obtener el Independent Set máximo (es decir, que contenga la mayor
cantidad de vértices) para el caso de un árbol (en el contexto de teoría de grafos, no un árbol binario). Indicar y
justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. Indicar si el
algoritmo siempre da solución óptima. Si lo es, explicar detalladamente, sino dar un contraejemplo."""

def independent_set_greedy(grafo):
    if len(grafo) == 1:
        return grafo.obtener_vertices()
    res = []
    hojas = set()
    # O(V) a lo sumo
    while grafo:
        if len(grafo) == 1:
            res.append(grafo.obtener_vertices()[0])
            break
        # O (V + E) --> es un arbol ---> O(V)
        for v in grafo:
            if len(grafo.adyacentes(v)) == 1:
                hojas.add(v)
                if len(grafo) == 2:
                    break
        # O(V) a lo sumo
        for hoja in hojas:
            padre = grafo.adyacentes(hoja)[0]
            if padre:
                grafo.borrar_vertice(padre)
            grafo.borrar_vertice(hoja)
            res.append(hoja)
        hojas.clear()
    
    return res

"""
El algoritmo planteado tiene una complejidad de O(V ** 2).

Se trata de un algoritmo greedy porque a través de la aplicación de una regla sencilla, buscamos obtener un óptimo local
al estado actual. En este caso, la regla sencilla es siempre agarrar las hojas del árbol y sumarlas a la solución dado nuestro
grafo actual (que vendría a ser el estado actual). De esta manera, buscamos obtener la mayor cantidad de vértices en la solución
(óptimo local) para el grafo actual. A través de aplicar iterativamente esta regla, esperamos llegar a un óptimo global, en este caso,
obtener el maximo independent set para el árbol.

El algoritmo planteado siempre obtiene la solución óptima debido a la naturaleza propia del árbol. Si buscamos ocupar la mayor
cantidad de vértices de manera que ninguno sea adyacente a otro, lo mejor sería ocupar los vértices que menos adyacentes tienen.
En el caso del árbol, estos son las hojas del mismo. Debido a la forma del árbol, utilizar las hojas para la solución siempre
será mucho más efectivo que usar los padres por ejemplo. Por cada nodo padre ocupado, perdemos la oportunidad de ocupar
los múltiples hijos que este podría tener. En cambio, en el caso de un nodo hoja, podemos ocupar esto y solo perdemos
la oportunidad de ocupar el nodo padre. Por ende, podríamos ocupar todos las hojas hijas de ese nodo padre sin problema.
Es importante notar que al remover nodos del árbol, este sigue siendo un árbol y esto permite que aparezcan nuevas hojas
para seguir aplicando esta regla.
"""

"""
Implementar un algoritmo que dado un grafo, obtenga el clique de mayor tamaño del mismo.
"""
def kclique(grafo):
    return _kclique(grafo, list(grafo.obtener_vertices()), [], [], 0)

def _kclique(grafo, vertices, solucion, conjunto_act, i):
    if i == len(vertices):
        if len(conjunto_act) > len(solucion):
            return list(conjunto_act)
        return list(solucion)
    
    conjunto_act.append(vertices[i])
    if not conjunto_act or es_clique(conjunto_act, grafo, vertices[i]):
        solucion = _kclique(grafo, vertices, solucion, conjunto_act, i+1)
    conjunto_act.pop()
    return _kclique(grafo, vertices, solucion, conjunto_act, i+1)

def es_clique(conjunto, grafo, vertice_act):
    for v in conjunto:
        if v == vertice_act:
            continue
        if not v in grafo.adyacentes(vertice_act):
            return False
    return True

""" 4) El problema de Subgrafo Isomórfico es el siguiente: Dado un grafo G1 y otro grafo G2, 
¿existe un subgrafo de G1 que sea isomorfo a G2? En el ejemplo del dorso, G2 es isomorfo al subgrafo de 
G1 que contiene a v0, v1, v2; G3 es isomorfo al subgrafo de G1 que contiene a v1, v2, v3; mientras que 
G4 no es isomorfo a ningún subgrafo de G1.
Demostrar que el problema de Subgrafo Isomórfico es un problema NP-Completo. Recomendación: Recordar que el
problema de K-Clique es un problema NP-Completo."""

"""
Para demostrar que el problema de SubGrafo Isomórifco es un problema NP-Completo, son necesarios dos pasos:
I) Demostrar que el problema es NP
Para esto es necesario implementar un verificador en tiempo polinomial. 
Dado un subgrafo G1 y un grafo G2, podríamos recorrer el subgrafo G1 y verificar que:
1) La cantidad de vértices de G1 es igual a la cantidad de vértices de G2
2) Cada vértice de G1 tiene la misma cantidad de adyacentes que el vértice correspondiente en G2.
Para ello es necesario recorrer todos los vértices de G1 y verificar que se cumplan las condiciones anteriores.
Esto se lograría en tiempo polinomial, por lo que el problema es NP.

II) Demostrar que el problema es NP-Completo

Primero debemos definir los problemas de decisión:

SubGrafo Isomórfico: Dados dos grafos G1 y G2, ¿existe un subgrafo de tamaño al menos k en G1 que sea isomorfo a G2?
K-Clique: Dado un grafo G y un número k, ¿existe un clique de tamaño al menos k en G?

Subgrafo Isomórfico <= p K-Clique

Para realizar la reducción es necesario reducir un problema NP-Completo a SubGrafo Isomórfico. En este caso, la recomendacion
es reducir K-Clique a SubGrafo Isomórfico.

Vamos a utilizar una caja negra que resuelve el problema de SubGrafo Isomórfico para resolver K-Clique.
Este recibe dos grafos, por lo tanto hay que transformar el problema.
Transformaremos el grafo del cual queremos saber si hay K-Clique a un grafo completo de K vértices, donde todos los vértices son adyacentes entre sí.
Nuestro grafo G1 será el grafo completo de k vértices y G2 será el grafo original.

Por lo tanto: Hay K-Clique en G si y solo si hay solución en SubGrafo Isomórfico entre G completo y G.

a. Hay K-Clique en G => Hay solución en SubGrafo Isomórfico entre G completo y G
Si hay K-Clique en G, entonces el grafo completo de K vértices será un subgrafo isomorfo a G, 
ya que todos sus vértices son adyacentes entre sí y dichos vértices y aristas existen en G.

b. Hay solución en SubGrafo Isomórfico entre G completo y G => Hay K-Clique en G
Si hay solución en SubGrafo Isomórfico entre G completo y G, quiere deir que el subgrafo de G
completo de al menos k vértices forma un K-Clique. Si este subgrafo es isomórfico a G, entonces quiere decir
que hay K-Clique en G.

Por lo tanto, hemos demostrado que SubGrafo Isomórfico es NP-Completo.
"""

grafo = Grafo(dirigido=True,vertices_iniciales=[1,2,3,4,5])
grafo.agregar_arista(1,2)
grafo.agregar_arista(1,4)
grafo.agregar_arista(2,4)
grafo.agregar_arista(2,5)
grafo.agregar_arista(3,4)
grafo.agregar_arista(4,5)
print(camino_mas_largo(grafo, [1,2,3,4,5]))



        
    
