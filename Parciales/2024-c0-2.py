from grafo import Grafo

"""
Un algoritmo sencillo para multiplicar matrices de n x n demora O(n
3). El algoritmo de Strassen (que utiliza División y Conquista) lo hace en O(n
log2 7). La profesora Manterola quiere implementar un algoritmo de División y Conquista que
sea aún más veloz, donde divida al problema en A subproblemas de tamaño de n 8, y que juntar las soluciones parciales
sea O(n 2). ¿Cuál es el máximo A para que el orden del algoritmo sea menor que el del algoritmo de Strassen? Justificar.
"""

"""
Teorema maestro:

Ecuación de recurrencia:
T(n) = A T(n / B) + O(n ** c)

A = cantidad de llamados recursivos
B = tamaño en el que se divide el problema original
O(n ** c) = El costo de partir y juntar

En este caso, el algoritmo propuesto por la profesora Manterola, se divide al problema en subproblemas de tamaño n / 8 y
el costo de juntar las soluciones es O(n ** 2). Por lo que:

A = ?
B = 8
C = 2

queremos que el algoritmo sea mejor que O(n ** log 2 (7)) --> O(n ** 2.81)

log b (a) < c ---> O(n ** c) a lo sumo es O(n ** 2) si esto se cumple. No nos sirve para encontrar el máximo A para que el orden
siga siendo mejor.

log b(a) = c ---> O(n ** c * log n) esto se traduce si o si en O(n ** 2 * log n)

log b(a) > c ---> O(n ** log b (a)). Como A aparece como variable en la complejidad, es más probable que el valor máximo de A
salga de esta ecuación.

Teniendo en cuenta que B = 8 y C = 2, necesitamos buscar log 8 (A) > 2 y log 8 (A) < log 2 (7)
Como buscamos el máximo, nos interesará más la segunda ecuación.
El valor máximo que puede tomar A es 343. En dicho valor, la complejidad temporal del algoritmo propuesto queda igual a la de
Strassen, por lo que A puede ser como mucho 342 para seguir siendo menor en orden que el de Strassen.
"""

"""
El papá de Pepe le dió n monedas para repartir entre él y su hermanito. El padre puso las monedas formando una
única fila. Cada moneda tiene con diferente valor vi.

El padre de Pepe le dice que primero debe elegir una para él,
y que sólo puede elegir la primera o la última de la fila. Luego, debe elegir una para su hermano menor siguiendo la
misma regla, luego otra para él, y así.
Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor máximo que pueda quedarse Pepe
dadas estas condiciones (asumamos que usará parte de sus ganancias para comprarle un chocolate a su hermano).
Importante: antes de escribir código, plantear y explicar la ecuación de recurrencia correspondiente.
"""

"""
OPT(N,i,j) = OPT(N - 1) + max(i,j)

Donde N es el numero del turno de Pepe, i es la moneda que se encuentra primera en la fila y j es la moneda que se encuentra
última. Es importante notar que si N == 0, la parte de OPT(N - 1) es 0

Lo que haremos será tomar la mayor moneda en el turno de Pepe y sumarla al valor que él llevaba acumulado durante previos turnos.
Cuando juguemos por el hermano menor de Pepe, simplemente agarraremos la moneda más chica
"""

def pepe_monedas(monedas):
    res = [0] * (len(monedas) // 2)
    if len(monedas) % 2 != 0:
        res.append(0)
    turno = 0
    i = 0
    j = len(monedas) - 1
    while turno < len(monedas) // 2:
        # Turno de pepe, agarra la más grande posible y lleva cuenta de cuanto acumuló
        res[turno] = res[turno - 1] + max(monedas[i], monedas[j]) if turno - 1 >= 0 else max(monedas[i], monedas[j])
        if monedas[i] > monedas[j]:
            i += 1
        else:
            j -= 1
        # Turno del hermano menor de Pepe, simplemente agarra la mas chica
        if monedas[i] < monedas[j]:
            i += 1
        else:
            j -= 1
        turno += 1
    
    if len(monedas) % 2 != 0:
        res[turno] = res[turno - 1] + monedas[i]
    return res[-1]

print(pepe_monedas([20,30,15,50]))

"""
Implementar un algoritmo Greedy que busque aproximar la solución óptima al problema del mínimo Vertex Cover:
dado un grafo, obtener el mínimo Vertex Cover del mismo. Indicar la complejidad del algoritmo implementado, dar un
contraejemplo para el algoritmo implementado y justificar por qué el algoritmo implementado es un algoritmo greedy.
"""

def min_vertex_cover(grafo):
    res = []
    cambio = True
    # O(V) a lo sumo (todos vértices que tengan aristas a si mismos)
    while cambio:
        cambio = False
        max = 0
        max_vertice = None
        # O (V + E), por cada vértice vemos sus adyacentes
        for v in grafo:
            if len(grafo.adyacentes(v)) > max:
                max = len(grafo.adyacentes(v))
                max_vertice = v
                cambio = True
        if not cambio:
            break
        res.append(max_vertice)
        grafo.borrar_vertice(v)
    return res

grafo = Grafo(False, False, [1,3,2,4,5])
grafo.agregar_arista(1,2)
grafo.agregar_arista(2,3)
grafo.agregar_arista(3,4)
grafo.agregar_arista(4,5)
print(min_vertex_cover(grafo))

"""
La complejidad del algoritmo planteado es a lo sumo O(V ** 2).

El contraejemplo para este algoritmo es por ejemplo:

1--2--3--4--5

La solución óptima sería elegir el 2, luego el 4 y tenemos todas las aristas cubiertas. Sin embargo,
al elegir siempre el vértice con más grado, podríamos empezar eligiendo el 3, con lo cual terminaríamos con la solución
[3, 4, 2], la cual no es óptima.


Se trata de un algoritmo greedy porque se aplica una regla sencilla que nos permite obtener el óptimo local según nuestro estado
actual. En este caso, buscamos el vértice con mayor grado del grafo actual, que vendría a ser como nuestro estado actual. Al
encontrar dicho vértice, lo agregamos a la solución y lo removemos del grafo, obteniendo otro estado nuevo al cual aplicar la
misma lógica. A través de la aplicación iterativa de esta regla sencilla, buscamos conseguir el óptimo general, en este caso,
obtener el min vertex cover.
"""


"""
Indicar si las siguientes afirmaciones sobre Redes de Flujo son verdaderas o falsas, justificando detalladamente.
a. Si aumentamos la capacidad de todas las aristas por una constante K, implicará que el flujo máximo aumente en
[K x min (grado_salida[fuente], grado_entrada[sumidero])] unidades.
b. En el caso del flujo máximo de la red, aumentarle la capacidad a una arista cuya capacidad no fue consumida no
tienen ningún efecto sobre el flujo máximo.
c. Eliminar una arista al azar del grafo puede no afectar el flujo máximo, pero si eliminamos una arista que es parte
del corte mínimo, entonces obligatoriamente sí afectará al flujo máximo.

a. Falso, que el flujo máximo aumente depende del corte mínimo, no del grado de salida de la fuente y el grado de entrada del
sumidero
b. Verdadero, al aumentarle la capacidad, no habrá cambio en el flujo máximo dado a que el corte que no permite que haya mayor
flujo estará en otra parte, no en esa arista.
c. Verdadero, si eliminamos una arista que no es utilizada, no afectará el flujo máximo por ejemplo. Si eliminamos una arista
que es parte del corte mínimo, si estaremos afectando al flujo máximo dado que esa arista permitía que circule más flujo
hacia el sumidero, por lo que si la removemos, el flujo máximo será menor. El flujo no tiene otro lugar por el que moverse
si eliminamos esa arista.
"""
        
        
        



