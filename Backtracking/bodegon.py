def max_grupos_bodegon(P, W):
    res = []
    return subset_sum(P, 0, W, res, [])

def subset_sum(P, indice, W, conjunto_actual, conjunto_maximo):
    if sum(conjunto_actual) == W:
        return conjunto_actual
    
    if indice == len(P):
        if sum(conjunto_actual) > sum(conjunto_maximo):
            return conjunto_actual
        return conjunto_maximo
    
    grupo_actual = P[indice]
    conjunto_actual.append(grupo_actual)
    if sum(conjunto_actual) <= W:
        conjunto_maximo = list(subset_sum(P, indice + 1, W, conjunto_actual, conjunto_maximo))
    conjunto_actual.pop()
    if sum(conjunto_maximo) == W:
        return conjunto_maximo
    return subset_sum(P, indice + 1, W, conjunto_actual, conjunto_maximo)

print(max_grupos_bodegon([5,3,2,8,2,5,6], 17))