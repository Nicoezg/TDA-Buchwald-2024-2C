def scheduling(charlas):
    charlas.sort(key=lambda x: x[1])
    p = [0]
    valores = [0]
    for i in range(len(charlas)):
        p.append(calcular_compatibilidad(charlas[i], charlas, 0, len(p) - 1))
        valores.append(charlas[i][2])
    
    M_SCHE = sche_dinamico(len(charlas), p, valores)
    return sche_solucion(M_SCHE, valores, p, len(valores) - 1, [], charlas)[::-1]

def sche_dinamico(n, p, valor):
    if n == 0:
        return 0
    M_SCHE = [0] * (n + 1)
    M_SCHE[0] = 0
    for j in range (1, n + 1):
        M_SCHE[j] = max(valor[j] + M_SCHE[p[j]], M_SCHE[j-1])
    return M_SCHE

def calcular_compatibilidad(charla_a_agregar, charlas, ini, fin):
    if ini > fin:
        return ini
    medio = ini + (fin - ini) // 2
    if charla_a_agregar[0] >= charlas[medio][1] and charla_a_agregar[0] < charlas[medio + 1][1]:
        return medio + 1
    if charla_a_agregar[0] < charlas[medio][1]:
        return calcular_compatibilidad(charla_a_agregar, charlas, ini, medio - 1)
    return calcular_compatibilidad(charla_a_agregar, charlas, medio, fin)

def sche_solucion(M_SCHE, valor, p, j, solucion, charlas):
    if j == 0:
        return solucion
    if valor[j]+M_SCHE[p[j]] >= M_SCHE[j-1]:
        solucion.append(charlas[j - 1])
        return sche_solucion(M_SCHE, valor, p, p[j], solucion, charlas)
    else:
        return sche_solucion(M_SCHE, valor, p, j-1, solucion, charlas)

print(scheduling([[0,3,2], [1,5,4], [4,5,4], [2,7,7], [6,8,2], [6,8,1]]))
        

