from grafo import Grafo

"""
Se tiene una matriz de n x m casilleros, en la cual empezamos en la posición (0, 0) (arriba a la izquierda) y queremos
llegar a la posición (n - 1, m - 1) (abajo a la derecha), pero solamente nos podemos mover hacia abajo o hacia la
derecha, y comenzamos con una vida inicial V . Cada casillero puede estar vacío, o tener una trampa. En los casilleros
que hay trampas se nos reduce la vida en una cantidad Ti conocida (dependiente de cada casillero).
Diseñar un algoritmo de programación dinámica que dados todos los datos necesarios, permita determinar la cantidad
de vida máxima con la que podemos llegar a (n - 1, m - 1). Implementar también una forma de poder reconstruir dicho
camino. Indicar la complejidad del algoritmo propuesto, en tiempo y espacio.
"""

def matriz_juego(matriz, V):
    res = []
    for i in range(len(matriz)):
        nueva_fila = []
        for j in range(len(matriz[0])):
            nueva_fila.append(0)
        res.append(nueva_fila)
    res[0][0] = V
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == 0 and j == 0:
                continue

            if i >= 1 and j >= 1:
                res[i][j] = max(res[i - 1][j], res[i][j - 1]) - matriz[i][j]
            
            elif i >= 1 and j < 1:
                res[i][j] = res[i - 1][j] - matriz[i][j]

            else:
                res[i][j] = res[i][j - 1] - matriz[i][j]

    return reconstruir_camino(res), res[-1][-1]

def reconstruir_camino(res):
    i = len(res) - 1
    j = len(res[0]) - 1
    camino = []

    while i > 0 or j > 0:
        camino.append((i, j))
        if i > 0 and j > 0:
            if res[i - 1][j] > res[i][j - 1]:
                i -= 1
            else:
                j -= 1
        elif i > 0 and j <= 0:
            i -= 1
        else:
            j -= 1
    return camino

matriz = [[0,0,0,0,10],
          [50,0,0,0,30],
          [10,20,10,20,10],
          [10,20,10,20,10],
          [10,0,0,0,0]
          ]

print(matriz_juego(matriz, 100))

"""
Todos los años la asociación de Tiro con Arco profesional realiza una preclasificación de los n jugadores que terminaron
en las mejores posiciones del ranking para un evento exclusivo. En la tarjeta de invitación quieren adjuntar el número de
posición en la que está actualmente y a cuántos rivales invitados logró superar en el ranking, en comparación al ranking
del año pasado. Contamos con un listado que tiene el nombre del jugador y la posición del ranking del año pasado
ordenado por el ranking actual. Implementar un algoritmo que dada la lista mencionada, devuelva (por ejemplo, en un
diccionario) a cuántos rivales ha superado cada uno de los invitados. Para realizar esto de forma eficiente, recomendamos
utilizar División y Conquista.
Ejemplo: LISTA: [(A, 3), (B, 4), (C, 2), (D, 8), (E, 6), (F, 5)]. Se puede ver que el jugador A pasó del
3er lugar al 1er lugar, superando al jugador C. El jugador B llegó al segundo lugar y superó al jugador C. El jugador C
no logró superar a ninguno de los invitados (si bien se encuentra en la tercera posición, ya tenía el año anterior mejor
clasificación que el resto de invitados, por tanto no logró superar a ninguno), etc. . .
"""

def contar_inversiones(A, B):
    if len(B) <= 1:
        return dict()
    medio = len(B) // 2
    izq, der = B[:medio], B[medio:]
    dict_izq = contar_inversiones(A, izq)
    dict_der = contar_inversiones(A, der)
    res = dict()
    for jugador, superados in dict_izq.keys():
        res[jugador] = res.get(jugador, 0) + superados
    for jugador, superados in dict_der.keys():
        res[jugador] = res.get(jugador, 0) + superados
    return _contar_inversiones(izq, der, res)
    


def _contar_inversiones(l1, l2, dicc):
    contador = 0
    i = 0
    j = 0
    while i < len(l1):
        if j >= len(l2):
            j = 0
            i += 1
        if i >= len(l1):
            break
        if l1[i] > l2[j]:
            dicc[l1[i]] = dicc.get(l1[i], 0) + 1
        j += 1
    return contador

"""
El K-core de un grafo es el subgrafo del mismo en el cuál todos los vértices tienen grados mayor o igual a K. Implementar
un algoritmo greedy que dado un grafo y un valor K devuelva el K-core del grafo (es decir, el subgrafo en el cuál todos
los vértices involucrados tienen grado mayor o igual a K, en dicho subgrafo). Indicar y justificar la complejidad del
algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.
"""

def k_core(grafo, K):
    cambio = True
    while cambio: # O(V), en el peor de los casos, en cada iteración se borra un solo vértice.
        cambio = False
        for v in grafo: # O(V + E), vemos para cada vértice sus adyacentes
            if len(grafo.adyacentes(v)) < K: # O(1)
                grafo.borrar_vertices(v) # O(1)
                cambio = True
    return grafo

"""
La compeljidad del algoritmo propuesto es O(V * (V + E)) --> O(V ** 2).

Se trata de un algoritmo greedy porque a través de la aplicación de una regla sencilla, obtenemos un óptimo local segun el estado
actual. En este caso, la regla sencilla es remover los vértices que tengan menor grado que K, con lo cual obtenemos el óptimo local
para el grafo en ese estado. Nuestro estado actual será dado por el estado del grafo, al cual le iremos removiendo vértices.
A través de aplicar esta regla iterativamente, esperamos llegar al óptimo general, que en este caso sería obtener el k-core del
grafo.
"""

"""
Un director de teatro tiene un elenco de n actores para realizar sus obras (todos los actores se encuentran capacitados
para ello). Para cada obra necesita diferente cantidad de actores. Para evitar problemas en el elenco, decide que nunca
repetirá para una obra 2 actores que ya hayan participado juntos en una obra previa. El problema de los actores dice:
“Dado un conjunto de n actores y la información de en cuáles obras actuaron, ¿existe forma de seleccionar k de ellos
para hacer la siguiente obra, sin que existan dos de ellos que hayan compartido elenco previamente?”.
Demostrar que el problema de los actores es un problema NP-Completo.
"""

"""
Para demostrar que el problema de los actores es un problema NP-Completo es necesario:
I) Demostrar que el problema está en NP
II) Reducir un problema en NP-Completo al problema de los actores

Para I), es necesario poder implementar un verificador del problema de los actores, que dada una solución de dicho problema,
indique si es válida en tiempo polinomial en función de las variables del problema
"""

def es_solucion_actores(actores, solucion, k):
    # Si no se pudo conseguir K actores para la obra, no es solución
    if len(solucion) < k:
        return False
    # Nos fijamos que los actores existan realmente
    for actor in solucion:
        if actor not in actores:
            return False

    visitados = set()
    # Nos fijamos si el actor esta en la solución. Si está en la solución, no puede haber
    # otro actor que haya participado en alguna de las obras que participó dicho actor.
    for actor, obras in actores:
        if actor in solucion:
            for obra in obras:
                if obra in visitados:
                    return False
                visitados.add(obra)
    
    return True


"""
Determinamos la complejidad del verificador
- Fijarnos si la solución es < K es O(1)
- Fijarse si los actores que son parte de la solucion realmente son actores O(A) siendo A la cantidad de actores
- Fijarse que los actores que son parte de la solución no hayn participado de la misma obra O(A + O), siendo O la cantidad
de obras. Por cada actor vemos todas sus obras.

Por lo tanto, la complejidad es O(A + O). Por lo que el verificador es efectivamente polinomial. Esto implica que demostramos
que el problema de los actores se encuentra en NP.

Para demostrar II) es necesario elegir un problema que se encuentre en NP completo para reducirlo al problema de los actores.
En este caso, usaremos el problema de Independent Set de al menos tamaño K.

Independent Set de al menos K: Dado un grafo, determinar si es posible dar un conjunto de vértices de tamaño al menos K tal que
todos sus vértices pertenezcan al grafo y no sean adyacentes entre sí.

Buscamos:

Independent Set de al menos K <= p Problema de los actores

Para proseguir con la reducción, será necesario transformar el problema de manera que podamos solucionarlo con la caja negra
que resuelve el problema de los actores.

Para ello, pensaremos cada vértice del grafo como un actor, y los adyacentes de cada vértice serán los actores con los que ya 
ha actuado cada actor. El K será el mismo pero en el contexto del problema de los actores.

Entonces:
Si hay I.S. de al menos K <====> Hay solución al problema de los actores

Para esto, es necesario demostrar tanto la ida como la vuelta:

Ida) Si tenemos un I.S. de al menos K, significa que en el problema transformado para los actores, se pudo seleccionar al menos
k actores, los cuales eran vértices del grafo original, tal que ninguno de los actores haya actuado en la misma obra antes. Esto
último implica que los actores (vértices del grafo original) no actuaron nunca en una obra juntos (no son adyacentes en el grafo
original)

Vuelta) Si hay solución al problema de los actores con el problema transformado, significa que pudimos asignar k actores (vértices
del grafo original) tal que ninguno de los actores haya actuado junto a otro en otra obra (es decir, no son adyacentes en el grafo 
original). Por lo que podemos afirmar que hay solución para el I.S. de al menos K vértices.

Por lo tanto, habiendo demostrado I) y II) podemos afirmar que el problema de los actores es un problema NP-Completo
"""



        

    
