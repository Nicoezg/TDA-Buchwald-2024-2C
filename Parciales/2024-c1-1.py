from grafo import Grafo

"""1. Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar
tres días seguidos. Se tiene la información de la ganancia del día i (Gi), para cada día. Implementar un modelo de
programación lineal que maximice el monto a ganar por Juan, sabiendo que no aceptará trabajar tres días seguidos."""
"""
Definimos las variables binarias t_i, que indican si trabajará el dia i.
 Si trabaja el día i podrá sumar la ganancia i.
Además, definimos las restricciones:
- La sumatoria de t_i, t_i - 1 y t_i - 2 debe ser siempre <= 2, para que no trabaje tres días seguidos.
- Lo de arriba aplica para todo i >= 2 siendo i los indices de los trabajos
Una vez definidas las restricciones, definimos la función objetivo que será maximizar la ganancia total. Para ello,
sumamos la ganancia de cada día multiplicada por la variable binaria t_i, indicando si trabajó o no ese día.
"""


"""
Implementar un algoritmo greedy que permita obtener el mínimo del problema del viajante: dado un Grafo pesado G y
un vértice de inicio v, obtener el camino de menor costo que lleve a un viajante desde v hacia cada uno de los vértices
del grafo, pasando por cada uno de ellos una única vez, y volviendo nuevamente al origen. Se puede asumir que el grafo
es completo. Indicar y justificar la complejidad del algoritmo implementado.
¿El algoritmo obtiene siempre la solución óptima? Si es así, justificar detalladamente, sino dar un contraejemplo. Indicar
y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.
"""

def problema_viajante(grafo, v):
    visitados = set()
    visitados.add(v)
    camino = [v]
    while len(camino) < len(grafo):
        minimo = float('inf')
        for w in grafo.adyacentes(v):
            if w not in visitados and grafo.peso_arista(v, w) < minimo:
                minimo = grafo.peso_arista(v, w)
                u = w
        visitados.add(u)
        camino.append(u)
        v = u
    return camino

"""
La complejidad del algoritmo es de O(V + E), siendo V la cantidad de vértices y E la cantidad de aristas del grafo.
Recorremos cada vértice, y en cada vértice nos fijamos sus adyacentes, por lo que la complejidad es la mencionada.
Las operaciones de agregar a visitados, obtener pesos de aristas, agregar a una lista y demás son O(1).

El algoritmo greedy siempre obtiene la solución óptima si consideramos que el grafo es completo. Esto se debe a que
cada vértice está conectado a todos los demás, por lo que siempre se elegirá la arista de menor costo. Al tener que visitar
todos los vértices y al estar todos conectados entre sí, al elegir una arista, no "perdemos" la posibilidad de una posible mejor solución.

El algoritmo planteado es greedy debido a que aplica una regla sencilla, en este caso, en cada vértice, se elige la arista de menor peso.
Esto nos permite obtener el óptimo local al estado actual. Aplicando iterativamente esta regla, se espera llegar al óptimo general (la mejor
solución posible)
"""
grafo = Grafo(pesado=True, vertices_iniciales = [1,2,3])
grafo.agregar_arista(1,2,2)
grafo.agregar_arista(2,3,1)
grafo.agregar_arista(1,3,10)


print(problema_viajante(grafo, 1)) # Debería devolver [1,2,3] o [1,3,2] con costo 10

"""
4) Implementar un algoritmo potencia(b, n) que nos devuelva el resultado de b n en tiempo O(log n). Justificar
adecuadamente la complejidad del algoritmo implementado. Ayuda: recordar propiedades matemáticas de la potencia.
"""

def potencia(b, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return potencia(b * b, n // 2)
    return b * potencia(b, n - 1)
    
print(potencia(6, 2))

# Por teorema maestro
# A: cantidad de llamados recursivos : 1
# B: division del problema : 2
# C: costo de partir y juntar: 0 (O(1))

#--> T(n) =  A * T(n/B) + O(n^C) ---> T(n) = 1 * T(n/2) + O(1)
# log b A = C ---> log 2 1 = 0 ----> el algoritmo propuesto es O(log n)

"""
Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
utilizando programación dinámica. Indicar y justificar la complejidad del algoritmo implementado (cuidado con esto, es
fácil tentarse a dar una cota más alta de lo correcto). Implementar un algoritmo que permita reconstruir la solución.
Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1
2
, por lo que siempre existe solución.

Sin embargo, la expresión 10 = 32 + 12

es una manera más económica de escribirlo para n = 10, pues sólo tiene dos

términos.
"""
# Lo transformo similar al problema del cambio
def suma_cuadrados(n):
    i = 1
    cant = [0] * (n + 1)
    cuadrados = []
    while i * i <= n:
        cuadrados.append(i * i)
        i += 1
    
    for i in range(1, n + 1):
        minimo = i # Usar todas de 1.
        for cuadrado in cuadrados:
            if cuadrado > i:
                continue
            cantidad = 1 + cant[i - cuadrado]
            if cantidad < minimo:
                minimo = cantidad
        cant[i] = minimo
    return reconstruir(cant, cuadrados, n)

def reconstruir(cant, cuadrados, n):
    res = []
    n_act = n
    for i in range(len(cuadrados) - 1, -1, -1):
        if cuadrados[i] > n:
            continue
        if n_act == 0:
            break
        if cant[n_act - cuadrados[i]] + cant[cuadrados[i]] <= cant[n_act]:
            while n_act >= cuadrados[i]:
                res.append(int(cuadrados[i] ** 0.5))
                n_act -= cuadrados[i]
    return res

print(suma_cuadrados(10)) # Debería devolver [3,1]

"""
Coty cumplió años ayer y está organizando su festejo. En dicho festejo, va a dar unos regalos. Son regalos geniales,
que van a dar que hablar luego del festejo. Eso es justamente lo que desea ella: que todos aquellos invitados que se
conozcan entre sí, luego de terminado el evento hablen del regalo que recibió uno, o bien el otro. ¿El problema? Coty
está invitando a n personas, pero no tiene presupuesto para comprar n regalos, sino tan sólo k.
El problema del cumpleaños de Coty puede enunciarse como: Dada la lista de n invitados al cumpleaños de Coty, un
número k, y conociendo quién se conocen con quién (ej: una lista con los pares de conocidos), ¿existe una forma de
asignar a lo sumo k personas para dar los regalos, de tal forma que todos los invitados, al hablar luego con quienes se
conozcan, puedan hablar del regalo que obtuvo uno o bien el otro?

Demostrar que el problema del cumpleaños de Coty es un problema NP-Completo.
"""

"""
Para demostrar que el problema de Coty es un problema NP-Completo, son necesarios dos pasos:
1) Demostrar que el problema esta en NP.

Para esto es necesario implementar un verificador en tiempo polinomial que verifique si dada la lista de n invitados,
conociendo quien se conoce con quien y a quienes le dieron regalo, pueda determinar si la solución es valida.
"""

def verificar_solucion(invitados, k, conocidos, solucion):
    inv_set = set(invitados) # O(i)
    if len(solucion) > k: # O(1)
        return False
    for elem in solucion: # O(k)
        if elem not in inv_set:
            return False
    
    for par in conocidos: # O(c)
        inv1, inv2 = par
        if inv1 not in solucion and inv2 not in solucion:
            return False
    return True

"""
La complejidad del algoritmo es de O(k + c + i), siendo i la cantidad de invitados, k la cantidad de regalos y c la cantidad de conocidos.
Por lo tanto, el problema ejecuta en tiempo polinomial, lo cual quiere decir que el problema se encuentra en NP.


2) Reducir un problema en NP-Completo al problema de Coty
En este caso, buscaremos reducir Vertex Cover, que sabemos que está en NP-Completo, al problema de Coty.
V.C. <= p Coty

Para realizar esta reducción, vamos a utilizar una caja negra que resuelve el problema del cumpleaños de coty para
resolver Vertex Cover. Este recibe un grafo y un valor k. Definimos:
- Un invitado I por cada vértice Vi del grafo. Pasamos una lista con esos invitados
- Un par de conocidos (Ii, Ij), si los vértices Vi y Vj a los que representan son adyacentes en nuestro grafo
- El valor del k' del problema del cumpleaños coincide con el valor del k recibido por el problema de VC.

Debemos demostrar que:
Hay solución de VC tamaño a lo sumo k <-> Hay solución de CC tamaño a lo sumo k' en la reducción dada.


A) Si hay VC de tamaño a lo sumo k, esto implica que todas las aristas estan cubiertas por un vértice en alguno de los extremos.
Si nosotros decidieramos darle regalo a esos vértices, que son a lo sumo k, cumplimos con la restriccion. A su vez, como las
relaciones entre conocidos fueron generadas a partir de las aristas del grafo, no puede suceder que haya un par de invitados
conocidos donde ninguno tenga regalo, porque eso implicaria que una de las aristas del VC no está cubierta, lo cual es absurdo.

B) Si hay solución de CC tamaño a lo sumo k' en la reducción dada implica que se puede dar regalo a k' personas de tal forma
que estas personas puedan hablar con sus conocidos sobre su regalo o el del otro. Teniendo en cuenta que k' = k, y que cada invitado
en el grafo representa un vértice, y que cada arista representa una relación de conocidos, si decimos que todas las personas
pudieron hablar de su regalo o el del otro con sus conocidos, implica que la arista está cubierta por un vértice en el grafo original.
"""






    

         
