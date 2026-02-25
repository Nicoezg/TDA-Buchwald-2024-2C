from grafo import Grafo

"""
Hitting set problem.

Dominating set es un problema NP-Completo. Desmotrar que hitting set problem es un problema NP-Completo,
utilizando dominating set para esto.

Para demostrar que hitting set problem es un problema NP-Completo, es necesario:
I) Demostrar que el problema esta en NP.
II) Reducir un problema NP-Completo a hitting set problem.

Para I), es necesario implementar un verificador del problema en tiempo polinomial segun las variables del problema
"""

def es_hitting_set(A, subconjuntos, k, solucion):
    # Si la solución tiene mas de k elementos, no es solucion
    if len(solucion) > k:
        return False
    
    # Nos fijamos que el conjunto solucion tenga al menos un elemento
    # de cada subconjunto
    for conjunto in subconjuntos:
        contiene_uno = False
        for elemento in conjunto:
            if elemento in solucion:
                contiene_uno = True
        if not contiene_uno:
            return False
    
    # Nos fijamos que cada elemento de la solución exista en A
    for elemento in solucion:
        if elemento not in A:
            return False
    
    return True

"""
- Fijarse que la solución no tenga más de K elementos es O(1)
- Fijarse que el conjunto solución tenga al menos un elemento de cada subconjunto
es O(C * E), siendo C la cantidad de subconjuntos de A y E la cantidad de elementos
de cada subconjunto.
- Verificar que cada elemento de la solución exista en A es a lo sumo O(K) siendo
K la cantidad de elementos en la solución.

Por lo cual, se puede afirmar que es posible implementar un verificador en tiempo polinomial
de acuerdo a las variables del problema. Por lo tanto, podemos decir que el problema de hitting set
se encuentra en NP.



II) Para la reducción, utilizaremos el problema de dominating set que se encuentra en NP-Completo.

===> dominating set <= p hitting set

Para realizar esta reducción, es necesario transformar el problema. Intentaremos resolver el problema
de dominating set utilizando una caja negra que resuelve el problema de is hitting set. Para ello, plantearemos
que el grafo que recibe el dominating set sea el A en el problema del hitting set, donde cada elemento será un
vértice del grafo. Los subconjuntos serán formados por los vértices que sean adyacentes entre sí en el grafo
original. Por último el k del problema de dominating set será el k del problema del hitting set.

Si hay solución de al menos K para dominating set <====> hay solución de al menos k para hitting set.

Es necesario demostrar ida y vuelta:

ida) Si hay solución de al menos K para dominating set, significa que se consiguieron al menos K vértices que
son adyacentes al resto de vértices del grafo o / y forman parte del mismo grafo. Ya que los subconjuntos en el
problema transformado son vértices adyacentes entre sí, esto quiere decir que si tenemos los vértices que son
adyacentes al resto de los vértices del grafo original, quiere decir que podemos conseguir una solución que
contenga al menos un elemento de cada subconjunto de al menos tamaño K.

vuelta) Si hay solución de al menos K vértices en el hitting set, significa que en nuestro conjunto solución
tenemos al menos un elemento de cada subconjunto que está formado por los vértices que son adyacentes entre sí.
Por ende, si es solución, tenemos al menos un vértice de cada uno de estos subconjuntos de adyacentes. Esto quiere
decir que encontramos al menos K vértices que en conjunto son adyacentes a todos los vértices del grafo original
y/ o forman parte de él. Por lo que tenemos solución de Dominating Set.

Habiendo reducido el problema de dominating set a hitting set y habiendo implementado un verificador de orden
polinomial de acuerdo a las variables del problema, podemos afirmar que hitting set es un problema NP-Completo

"""

def dominating_set_min_greedy(grafo):
    solucion = set()
    grados = dict()
    if len(grafo) == 1:
        return grafo.obtener_vertices()
    while grafo:
        hojas = set()
        # O(V + E) , E = V - 1 --> O(V), por cada vértice me fijo sus adyacentes
        for v in grafo:
            grados[v] = len(grafo.adyacentes(v))
            if grados[v] == 1:
                hojas.add(v)

        # O(V + E) , E = V - 1 ---> O(V) como mucho
        for hoja in hojas:
            if len(grafo.adyacentes(hoja) == 0):
                solucion.add(hoja)
            else:
                padre = grafo.adyacentes(hoja)[0]
                solucion.add(grafo.adyacentes(hoja)[0])
                # O(V + E), E = V - 1 ---> O(V) como mucho
                for adyacente in grafo.adyacentes(padre):
                    grafo.borrar_vertice(adyacente)
                grafo.borrar_vertice(padre)
"""
Se trata de un algoritmo greedy porque se aplica una regla sencilla que nos permite obtener el óptimo local
al estado actual. En este caso, nos aseguramos de que todas las hojas del grafo sean cubiertas por su padre
en el estado del grafo actual. Aplicando iterativamente esta regla, esperamos que nos lleve al óptimo general, que,
en este caso sería que el número de vértices del conjunto solución del problema de dominating set sea mínimo.

Siempre obtiene la solución óptima dado que la única forma de cubrir las hojas de un árbol en el problema de dominating set,
es eligiendo la hoja en sí (lo cual no nos dará el minimo dominating set, dado que estamos cubriendo la menor cantidad 
posible de vértices eligiendo dicha hoja) o eligiendo a su padre. Al quedarnos solo con estas dos opciones, y una claramente
siendo inútil para el problema planteado, elegir siempre al padre nos permitirá cubrir la hoja en el problema del dominating
set, otros posibles hijos que pueda tener ese padre y a su padre. Los vértices adyacentes al padre, ahora estarán cubiertos en el grafo,
por lo que pueden ser removidos, resultando que vértices que antes no eran hojas, ahora lo sean y se pueda volver a aplicar
la misma lógica previa. Siempre es mejor ocupar el padre antes que la hoja en sí dado que en un árbol, las hojas siempre tendrán
un único adyacente (su padre) y los padres de estas, al menos tienen dos adyacentes (su padre y su hijo). En caso de que
el padre no tenga al menos dos adyacentes, significa que el padre es la raíz del árbol.
"""


"""
Realizar un modelo de programación lineal que obtenga el mínimo Dominating Set de un Grafo no dirigido. En dicho
grafo, cada vértice tiene un valor (positivo), y se quiere que dicho Dominating Set sea el de mínima suma de dichos
valores.
"""

"""
Definiremos variables binarias, Vi que valdrán 1 si el vértice esta cubierto o 0 en caso contrario
Por otro lado, definiremos Bi, que valdrá 1 si el vértice es parte del dominating set o 0 en caso contrario
Nuestra función objetivo será minimizar la suma de los vértices ocupados.

Pediremos que la sumatoria de los Vi sea igual a la cantidad de vértices en el grafo, de manera que pediremos que
todos los vértices en el grafo esten cubiertos.

Si definimos nuestro problema como prob:

prob += B[i] * grafo[i]

Donde B contendrá las variables binarias Bi, de manera que si es parte del dominating set, valdrá su valor contenido
en el grafo. Si no es parte del dominating set, no sumará nada. Es importante notar que esta es la función a minimizar,
por lo que el resultado debería ser el mínimo
"""

"""
Implementar un algoritmo que (por backtracking) dado un grafo no dirigido en el que sus vértices tienen valores positivos,
permita obtener el Dominating Set de suma mínima. Es decir, aquel dominating set en el cual la suma de todos los
valores de los vértices sea mínima (no es importante que la cantidad de vértices del set sea mínima). Por simplicidad,
considerar que el grafo es conexo.
"""


def backtracking_suma_minima_ds(grafo):
    ds_minimo, mejor_valor = _backtracking_suma_minima_ds()
    return ds_minimo

def _backtracking_suma_minima_ds(grafo, vertices, i, conj_act, mejor_sol, valor_act, mejor_valor):
    if i == len(vertices):
        if valor_act < mejor_valor:
            return list(conj_act), valor_act
        return list(mejor_sol), mejor_valor
    
    vertice_actual = vertices[i]
    conj_act.remove(vertice_actual)
    if valor_act - sum(vertices[i::]) > mejor_valor:
        return list(mejor_sol), mejor_valor
    if es_dominating_set():
        mejor_sol, mejor_valor = _backtracking_suma_minima_ds(grafo, vertices, i + 1, conj_act, mejor_sol, valor_act - vertice_actual, mejor_valor)
    conj_act.append(vertice_actual)
    return _backtracking_suma_minima_ds(grafo, vertices, i + 1, conj_act, mejor_sol, valor_act, mejor_valor)
    
def es_dominating_set(grafo, conj_act):
    visitados = set()
    for v in conj_act:
        visitados.add(v)
        for w in grafo.adyacentes(v):
            visitados.add(w)

    return len(visitados) == len(grafo)

"""
Sea G un grafo dirigido “camino” (las aristas son de la forma (vi, vi-1)). Cada vertice tiene un valor (positivo).
Implementar un algoritmo que, utilizando programación dinámica, obtenga el Dominating Set de suma mínima
dentro de un grafo de dichas características. Dar la ecuación de recurrencia correspondiente al problema. Indicar
y justificar la complejidad del algoritmo implementado. Indicar y justificar la complejidad espacial del algoritmo
implementado, y si hay una optimización que permita consumir menos espacio.
"""
    
def suma_minima_camino(grafo):
    if len(grafo) == 0:
        return []
    if len(grafo) == 1:
        return [0]
    ganancia = [0] * len(grafo) # O(N) siendo N la cantidad de vértices en el grafo
    vertices = grafo.obtener_vertices()
    ganancia[0] = vertices[0]
    ganancia[1] = min(vertices[0], vertices[1])
    if ganancia[1] == vertices[0] and vertices[0] != vertices[1]:
        cubierto = False
    else:
        cubierto = True
    
    # O(N) nuevamente
    for d in range(2, len(vertices)):
        if not cubierto:
            ganancia[d] = ganancia[d - 1] + vertices[d]
            cubierto = True
            continue
        ganancia[d] = min(vertices[d] + ganancia[d-2], ganancia[d-1])
        if ganancia[d] == ganancia[d - 1]:
            cubierto = False
        else:
            cubierto = True
    return reconstruccion_min_dominating_set(ganancia, vertices)

def reconstruccion_min_dominating_set(camino, vertices):
    dominating_set = []
    largo = len(vertices) - 1
    # O(N)
    while largo >= 0:
        opt_previo = camino[largo - 1] if largo > 0 else 0
        opt_previo_previo = camino[largo - 2] if largo > 2 else 0
        opt_actual = camino[largo]

        if opt_previo_previo + vertices[largo] == opt_actual:
            dominating_set.append(vertices[largo])
        else:
            dominating_set.append(vertices[largo - 1])
        largo -= 2
    return dominating_set

"""
Ecuacion de recurrencia

OPT(N) = { min(vertices[n] + OPT(N - 2), OPT(N - 1)) if cubierto, vertices[n] + OPT(N - 1) if not cubierto}

Donde N es la cantidad de vértices en el camino, vertices la lista de vértices del grafo y cubierto es una variable
que es True si el vértice a colocar está cubierto por el anterior o si no está cubierto por el anterior.

La complejidad del algoritmo es O(N), siendo N la cantidad de vértices en el camino.
Esto se debe a que en todo momento hacemos operaciones O(1) y recorremos sobre el arreglo de largo N.

"""




    
        
