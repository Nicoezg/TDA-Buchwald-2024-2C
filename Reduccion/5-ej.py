"""
Para cada uno de los siguientes problemas, 
implementar un verificador polinomial y justificar su complejidad.

a. Dado un número por parámetro, si es la solución al problema de 
Búsqueda del máximo en un arreglo b. Dado un arreglo, si es la solución a 
tener el arreglo ordenado c. Dadas un arreglo de posiciones de Reinas, si es la solución de colocar al menos 
N-reinas en un tablero NxN
"""


def maximo(n, arr):
    max = None
    for elem in arr:
        if max is None or elem > max:
            max = elem
    return max == n

def ordenado(arr, c):
    for i in range(len(arr)):
        if arr[i] != c[i]:
            return False
    return True

def n_reinas(arr, n):
    grafo = grafo(arr)
    return verificador_indepent_set(grafo)