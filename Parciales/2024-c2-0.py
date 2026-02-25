"""Problema de la mochila usando backtracking"""

def mochila_cant_min(K, W, elementos):
    res, _ = _mochila_cant_min(K, W, elementos, 0, [], [], 0, 0, 0)
    return res
    
def _mochila_cant_min(K, W, elementos, indice, solucion_act, mejor_solucion, valor_actual, mejor_valor, peso_actual):
    if indice == len(elementos):
        if valor_actual > mejor_valor and len(solucion_act) >= K:
            return list(solucion_act), valor_actual
        if mejor_valor >= valor_actual and len(mejor_solucion) >= K:
            return list(mejor_solucion), mejor_valor
        return list(), 0
    
    peso, valor = elementos[indice]
    solucion_act.append(elementos[indice])

    if peso + peso_actual <= W:
        mejor_solucion, mejor_valor = _mochila_cant_min(K, W, elementos, indice + 1, solucion_act, mejor_solucion, valor_actual + valor, mejor_valor, peso + peso_actual)
    solucion_act.pop()
    return _mochila_cant_min(K, W, elementos, indice + 1, solucion_act, mejor_solucion, valor_actual, mejor_valor, peso_actual)

"""El problema de separación en R cliques (SRC) se enuncia como: Dado un grafo, y un valor entero R, se pueden
separar todos los vértices del grafo en a lo sumo R cliques? (cada clique puede tener una cantidad diferente de vértices).

Demostrar que el problema de Separación en R Cliques es un problema NP-Completo. Para esto, recomendamos recordar que el
problema de coloreo es un problema NP-Completo. También recomendamos recordar como fue que desmotramos en clase que K-Clique
es un problema NP-Completo (fue con la ayuda de I.S.)"""

"""
Para demostrar que el problema de Separación en R Cliques es un problema NP-Completo es necesario:
I) Separacion en R cliques tiene que estar en NP
II) Reducir un problema en NP-Completo a Separacion en R cliques.

Para I), es necesario lograr implementar un verificador en tiempo polinomial de acuerdo a las variables del problema.
"""

# La solucion es una lista de R cliques.
def es_r_clique(grafo, R, solucion):

    # Verificamos que efectivamente sean R cliques.
    if len(solucion) > R:
        return False
    
    # Verificamos que cada vértice de la solución se encuentre en el grafo original.
    for vertice in solucion:
        if vertice not in grafo:
            return False
    
    # En cada subconjunto, nos aseguramos que todos los vértices sean adyacentes entre ellos
    # y que efectivamente la arista exista en el grafo original
    for subconjunto in solucion:
        for i in range(len(subconjunto)):
            for j in range(i + 1, len(subconjunto) - 1):
                if not grafo.adyacentes(subconjunto[i], subconjunto[j]):
                    return False
                if not grafo.existe_arista(subconjunto[i], subconjunto[j]):
                    return False

    # Nos aseguramos de que los subconjuntos sean disjuntos.      
    visitados = set()
    for subconjunto in solucion:
        for v in subconjunto:
            if v in visitados:
                return False
            visitados.add(v)
    
    # Nos aseguramos de que todos los vértices del grafo se encuentren en el conjunto solucion
    return len(visitados) == len(grafo)

"""
- Verificar el largo del arreglo es O(1)
- Verificar que cada vértice que compone la solución se encuentre en el grafo original es O(V) siendo
V la cantidad de vértices del grafo original
- Verificar que efectivamente cada subconjunto sea un clique del grafo es a lo sumo O(R * (V + E)), siendo R el número
de cliques, V la cantidad de vértices del grafo original y E la cantidad de aristas. Es importante notar que es a lo sumo R,
dado que si era mayor que R, hubieramos cortado antes.
- Verificar que los subconjuntos sean disjuntos es a lo sumo O(R * V).
- Verificar que todos los vértices del grafo se encuentren en el conjunto solución una vez asegurado que no sean disjuntos es
O(1)

Por lo tanto, pudimos implementar un verificador en tiempo polinomial de acuerdo a las variables del problema. Esto quiere
decir que el problema se encuentra en NP.

II) Siguiendo la recomendacion del enunciado, buscaremos reducir el problema del coloreo a que se encuentra en NP-Completo al
problema de separación en R-Cliques (SRC).

===> coloreo <= p SRC.

Para realizar la reducción, es necesario transformar el problema. Transformaremos nuestro grafo original de coloreo en el grafo
complemento, donde todas las aristas existentes en el grafo original, no existen en el grafo complemento y todas las que no existen
en el grafo original, existen en el complemento.

Nuestro K del coloreo será el R en la transformación planteada. Le damos el grafo complemento y el K a la caja negra que resuelve
SRC.

Si hay solución de K coloreo <==> Hay solución de separación en R cliques.

Para realizar la reducción, es necesario demostrar el idea y vuelta

Ida) Si hay solución para K coloreo, significa que puedo asignarle un color distinto de los k disponibles a cada vértice sin que
ningún vértice comparta color con sus adyacentes. Esto quiere decir que en el grafo complemento, los vértices que en el original
están pintados con el mismo color, forman un clique, ya que si son adyacentes entre si en el grafo original. Por lo tanto, si
logré pintar con k colores en el grafo original, tendremos R cliques en el grafo complementario donde los vértices que tienen el
mismo color forman el clique.

Vuelta) Si hay solución para separación en R cliques, esto significa que cada vértice en cada conjunto de ese clique, no es
adyacente con los vértices de ese clique ene el grafo original. Lo que implica que se pueden pintar todos los de ese conjunto,
del mismo color, resultando en un K-coloreo en el grafo original, ya que a cada conjunto de los R, lo pinto de un color (K = R).

Dado I) y II), podemos afirmar que separación en R cliques es NP-Completo.

"""

"""
Programación dinámica: Osvaldo
"""

def osvaldo_dinamica(p):
    mejores_ventas = [0] * len(p)
    mejor_compra = p[0]
    indice_compra = 0
    indice_venta = 1
    for i in range(1,len(p)):
        mejores_ventas[i] = max(p[i] - mejor_compra, mejores_ventas[i - 1])
        if mejores_ventas[i] != mejores_ventas[i - 1]:
            indice_compra = p.index(mejor_compra)
            indice_venta = i
        if p[i] < mejor_compra:
            mejor_compra = p[i]
    return mejores_ventas[-1], indice_compra, indice_venta

print(osvaldo_dinamica([400, 200, 500, 600]))


"""
Osvaldo pero por division y conquista
"""

def max_subarray(arr):
    return _max_subarray(arr, 0, len(arr) - 1)

def _max_subarray(arr, ini, fin):
    if ini == fin:
        return [arr[ini]]
    medio = ini + (fin - ini) // 2
    izq = _max_subarray(arr, ini, medio)
    der = _max_subarray(arr, medio + 1, fin)
    suma_max_izq = None
    indice_izq = None
    suma_izq = 0
    suma_max_der = None
    indice_der = None
    suma_der = 0
    for i in range(medio, -1, -1):
        suma_izq += arr[i]
        if not suma_max_izq or suma_izq > suma_max_izq:
            indice_izq = i
            suma_max_izq = suma_izq
    for j in range(medio + 1, len(arr)):
        suma_der += arr[j]
        if not suma_max_der or suma_der > suma_max_der:
            indice_der = j
            suma_max_der = suma_der
    
    centro = arr[indice_izq : indice_der + 1]
    sum_izq = sum(izq)
    sum_der = sum(der)
    sum_cen = sum(centro)
    if sum_izq > sum_der and sum_izq > sum_cen:
        return izq
    if sum_der > sum_izq and sum_der > sum_cen:
        return der
    return centro


print(max_subarray([]))


    

        
    

    




