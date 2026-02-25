from grafo import Grafo

"""
Se define el problema 2-Partition de la siguiente manera: Se cuenta con un conjunto de n elementos. Cada uno de
ellos tiene un valor asociado. Se desea separar los elementos en 2 subconjuntos tal que la suma de los valores de cada
subconjunto sea igual para ambos.
2-Partition es un problema NP-Completo. Queremos demostrar nuevamente (pero de otra forma a la vista en clase) que
Subset Sum es un problema NP-Completo. Demostrar esto, utilizando que 2-Partition es un problema NP-Completo.

Para demostrar que Subset Sum es un problema NP-Completo, es necesario:
I) Demostrar que Subset Sum pertenece a NP
II) Reducir un problema en NP-Completo a Subset Sum

Para demostrar I) debemos implementar un verificador que dada una solución y la entrada del problema, verifique si efectivamente
la solución es correcta. Para esto, la complejidad del verificador debe ser polinomial.
"""

def es_subset_sum(conjunto, solucion, K):
    # Nos aseguramos que el conjunto solución sume K exactamente
    if sum(solucion) != K:
        return False
    visitados = dict()
    # Armamos un diccionario con el numero de apariciones de cada valor en el conjunto
    for valor in conjunto:
        visitados[valor] = visitados.get(valor, 0) + 1

    # Recorremos los valores en la solución, si no son parte del conjunto, no es una solución válida.
    # Si algún elemento aparece más veces de las que aparece en el conjunto original, tampoco es solución válida
    for valor in solucion:
        if not valor in conjunto:
            return False
        visitados[valor] = visitados.get(valor, 0) - 1
        if visitados[valor] < 0:
            return False
    return True

"""
A continuación, se analizará la complejidad del verificador propuesto:
- Sumar los valores de la solución y verificar si es igual a K --> O(N) a lo sumo, siendo N la cantidad de elementos en el conjunto
(caso de que la solucion sean todos los elementos del conjunto)
- Armar el diccionario con la cantidad de apariciones de los valores en el conjunto --> O(N).
- Recorrer los valores en la solución y verificar que los elementos no aparezcan más veces de las que están en el conjunto
---> O(N).

Por ende, la complejidad del verificador propuesto es O(N). Esto implica que su orden es polinomial, y por lo tanto, el problema
de Subset Sum se encuentra en NP


II) Reduciremos el problema de 2-Partition al problema de Subset Sum

Buscamos:

2-Partition <= p Subset Sum

Para ello, será necesario transformar el problema original para que sea posible utilizar la caja que resuelve el 
problema de Subset Sum. Primero, calcularemos la suma de todos los elementos que se le dieron al 2-Partition. 
Luego, le daremos una lista con todos los elementos y la suma de todos los elementos / 2 a subset-sum.

Planteamos:
Si hay solucion para 2-Partition <===> Hay solucion para Subset Sum

Es necesario demostrar el ida y vuelta.
Ida)
Si hay solución para 2-Partition, significa que hemos podido separar el conjunto de elementos en dos subconjuntos que
suman exactamente lo mismo. Esto se traduce a que en el problema transformado, habrá solución para el Subset Sum dado que
encontrará uno de los dos conjuntos del 2-Partition que sume exactamente la mitad de la suma de elementos totales.

Vuelta)
Si hay solución para Subset Sum en el problema transformado, quiere decir que encontró un conjunto de elementos tal que su suma
es la mitad de la suma total de elementos. Si encontró un conjunto que suma la mitad y la suma total de elementos es el doble,
quiere decir que hay otro conjunto distinto al encontrado que suma exactamente lo mismo. Por lo que podemos garantizar que hay
solución para 2-Partition

Dado I) y II), podemos afirmar que Subset Sum es un problema NP-Completo
"""

"""
En clase vimos una solución óptima del problema del cambio utilizando programación dinámica. Ahora planteamos un
problema similar: Implementar un algoritmo que dado un set de monedas posibles y una cantidad de cambio a dar,
devuelva la cantidad de formas diferentes que hay para dar dicho cambio. El algoritmo a implementar debe ser
también por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado. Importante: antes
de escribir código, escribir (y describir) la ecuación de recurrencia.
"""

"""
OPT(N) = OPT(N - 2) + OPT(N - 1)

Donde N es el monto a dar vuelto. Es importante notar que solo se aplica si N >= 3. Si N = 2, N = 1 o N = 0, los consideramos
como casos base.
N = 0 --> 0
N = 1 --> 1
N = 2 --> 2
"""

def diferentes_cambios(monedas, cambio):
    res = [0] * (cambio + 1)
    # Casos base
    res[0] = 0
    indice = 0
    if 1 in monedas:
        res[1] = 1
        res[2] = 1
        indice = 1
    if 2 in monedas:
        res[2] = 2
        indice = 2
    
    
    for i in range(3, cambio + 1):
        if indice < len(monedas) and i / monedas[indice] == 1:
            res[i] = res[i - 2] + res[i - 1] + 1
            continue
        res[i] = res[i - 2] + res[i - 1]
    return res

print(diferentes_cambios([1,2,5], 10))

"""
Implementar un algoritmo que reciba un grafo no dirigido y un número k, y devuelva un ciclo de tamaño exactamente k
del grafo, si es que existe.
"""

def ciclo_k(grafo, k):
    return _ciclo_k(grafo, k, list(grafo.obtener_vertices()), 0, [])

def _ciclo_k(grafo, k, v, solucion):
    if len(solucion) == k and solucion[0] in grafo.adyacentes(solucion[-1]):
        return list(solucion)
    if i == len(vertices):
        return []

    
    vertice_act = vertices[i]
    solucion.append(vertice_act)
    if len(solucion) <= k and (len(solucion) == 1 or vertice_act in grafo.adyacentes(solucion[-2])):
        solucion = _ciclo_k(grafo, k, vertices, i + 1, solucion)
        if solucion:
            return list(solucion)
    return _ciclo_k(grafo, k, vertices, i + 1, solucion)

# Esta mal
grafo = Grafo(False, False, [1,2,3,4])
grafo.agregar_arista(1,2)
grafo.agregar_arista(2,3)
grafo.agregar_arista(3,1)
grafo.agregar_arista(4,1)
print(ciclo_k(grafo, 4))


