# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    matriz = []
    for i in range(len(elementos) + 1):
        nueva_fila = []

        for j in range(W + 1):

            if j == 0 or i == 0:
                nueva_fila.append(0)
                continue
            peso = elementos[i - 1][1]
            valor = elementos[i - 1][0]

            if j - peso >= 0:
                if matriz[i - 1][j] <= matriz[i - 1][j - peso] + valor:
                    nueva_fila.append(matriz[i - 1][j - peso] + valor)
                else:
                    nueva_fila.append(matriz[i - 1][j])
            else:
                nueva_fila.append(matriz[i - 1][j])

            

        matriz.append(nueva_fila)
    res = []
    reconstruccion_mochila(matriz, elementos, res, len(matriz) - 1, len(matriz[0]) - 1)
    return list(reversed(res))
    
def reconstruccion_mochila(matriz, elementos, res, i, j):
    if i == 0:
        return
    if matriz[i][j] == matriz[i - 1][j]:
        return reconstruccion_mochila(matriz, elementos, res, i - 1, j)
    res.append(elementos[i - 1])
    return reconstruccion_mochila(matriz, elementos, res, i - 1, j - elementos[i - 1][1])

print(mochila([[58,7], [15,6], [51,12], [31,2], [13, 12], [89, 15], [19, 9], [4,12], [75, 8], [50,8]], 15))