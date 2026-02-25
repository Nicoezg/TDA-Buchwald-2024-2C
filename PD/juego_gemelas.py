from collections import deque

def plan_operativo(arreglo_L, arreglo_C, costo_M):
    londres = [0] * len(arreglo_L)
    california = [0] * len(arreglo_C)
    contador_londres = 0
    contador_california = 0
    matriz = [londres, california]
    for col in range(len(arreglo_L)):
        if col == 0:
            matriz[0][col] = arreglo_L[col]
            matriz[1][col] = arreglo_C[col]
            continue
        

        if matriz[0][col - 1] == arreglo_L[col - 1] + contador_londres:
        
            if arreglo_L[col] <= arreglo_C[col] + costo_M:
                matriz[0][col] = arreglo_L[col] + matriz[0][col - 1]
                contador_londres = matriz[0][col - 1]

            else:
                matriz[0][col] = arreglo_C[col] + costo_M + matriz[0][col - 1]
                contador_londres = matriz[0][col - 1]
                contador_londres += costo_M
        
        elif matriz[0][col - 1] != arreglo_L[col - 1] + contador_londres:

            if arreglo_C[col] <= arreglo_L[col] + costo_M:
                contador_londres = matriz[0][col - 1]
                matriz[0][col] = arreglo_C[col] + matriz[0][col - 1]

            else:
                matriz[0][col] = arreglo_L[col] + costo_M + matriz[0][col - 1]
                contador_londres = matriz[0][col - 1]
                contador_londres += costo_M
        
        if matriz[1][col - 1] == arreglo_C[col - 1] + contador_california:

            if arreglo_C[col] <= arreglo_L[col] + costo_M:
                contador_california = matriz[1][col - 1]
                matriz[1][col] = arreglo_C[col] + matriz[1][col - 1]

            else:
                matriz[1][col] = arreglo_L[col] + costo_M + matriz[1][col - 1]
                contador_california = matriz[1][col - 1]
                contador_california += costo_M

            
        else:

            if arreglo_L[col] <= arreglo_C[col] + costo_M:
                contador_california = matriz[1][col - 1]
                matriz[1][col] = arreglo_L[col] + matriz[1][col - 1]

            else:
                matriz[1][col] = arreglo_C[col] + costo_M + matriz[1][col - 1]
                contador_california = matriz[1][col - 1]
                contador_california += costo_M
    print(matriz)
                
    return reconstruir_rta(matriz, arreglo_L, arreglo_C, costo_M)
    

def reconstruir_rta(matriz, arreglo_L, arreglo_C, costo_M):
    res = []
    for i in range(0, len(arreglo_L)):
        if i == 0:
            if matriz[0][-1] < matriz[1][-1]:
                res.append("londres")
            else:
                res.append("california")
        
        elif res[i - 1] == "londres":
            
            if arreglo_L[i] < arreglo_C[i] + costo_M:
                res.append("londres")
            else:
                res.append("california")
        
        else:
            if arreglo_C[i] < arreglo_L[i] + costo_M:
                res.append("california")
            else:
                res.append("londres")
    return res

def juego(londres, california, costo):
    izq_sum = 0
    der_sum = 0
    
    # Convertimos las listas en deques para optimizar las operaciones
    izq_act = deque(londres)  # Sin la primera moneda
    der_act = deque(california)  # Sin la última moneda

    while True:
        if not izq_act or not der_act:
            break

        izq_der = izq_sum + izq_act[-1]
        der_der = der_sum + der_act[-1]
        der_izq = der_sum + der_act[0]
        izq_izq = izq_sum + izq_act[0]

        # Guardamos el estado actual para revertir si es necesario
        aux_izq_act = deque(izq_act)

        # Decisión para izq_sum
        if izq_izq >= der_izq:
            izq_sum = izq_izq
            izq_act.popleft()  # Elimina el primer elemento de izq_act
        else:
            izq_sum = der_izq
            izq_act = deque(der_act)
            izq_act.popleft()

        # Decisión para der_sum
        if der_der >= izq_der:
            der_sum = der_der
            der_act.pop()  # Elimina el último elemento de der_act
        else:
            der_sum = izq_der
            der_act = deque(aux_izq_act)
            der_act.pop()
    return max(izq_sum, der_sum)
londres = [5, 46, 18, 88, 33, 13, 22, 35, 58]
california = [20, 10, 65, 24, 55, 2, 28, 14, 94]


def lon_cal_pd(arreglo_L, arreglo_C, costo_M):
    mem_lon = [0] * (len(arreglo_L) + 1)
    mem_cal = [0] * (len(arreglo_C) + 1)

    mem_lon[1] = arreglo_L[0]
    mem_cal[1] = arreglo_C[0]

    for i in range(2, len(arreglo_L) + 1):
        mem_lon[i] = arreglo_L[i - 1] + min(mem_lon[i - 1], costo_M + mem_cal[i - 1])
        mem_cal[i] = arreglo_C[i - 1] + min(mem_cal[i - 1], costo_M + mem_lon[i - 1])

    return mem_lon, mem_cal


def reconstuccion(arreglo_L, arreglo_C, costo_M, mem_lon, mem_cal):
    index = len(arreglo_L)
    current = mem_lon[index] < mem_cal[index]
    resultado = []

    while index > 0:
        if current:
            resultado.append('londres')

            if mem_lon[index - 1] > mem_cal[index - 1] + costo_M:
                current = False
        else:
            resultado.append('california')

            if mem_cal[index - 1] > mem_lon[index - 1] + costo_M:
                current = True

        index -= 1

    resultado.reverse()
    return resultado


def plan_operativo2(arreglo_L, arreglo_C, costo_M):
    mem_lon, mem_cal = lon_cal_pd(arreglo_L, arreglo_C, costo_M)
    return reconstuccion(arreglo_L, arreglo_C, costo_M, mem_lon, mem_cal)

print(plan_operativo2([5, 46, 18, 88, 33, 13, 22, 35, 58], [20, 10, 65, 24, 55, 2, 28, 15, 94], 25))

def plan_operativo3(arreglo_L, arreglo_C, costo_M):
    n = len(arreglo_L)
    OPT_L = [0] * n
    OPT_C = [0] * n
    
    OPT_L[0] = arreglo_L[0]
    OPT_C[0] = arreglo_C[0]
    
    for i in range(1, n):
        OPT_L[i] = min(OPT_L[i-1] + arreglo_L[i], OPT_C[i-1] + arreglo_L[i] + costo_M)
        OPT_C[i] = min(OPT_C[i-1] + arreglo_C[i], OPT_L[i-1] + arreglo_C[i] + costo_M)
    
    # Reconstruccion de la solucion
    secuencia_localizaciones = [None] * n
    if OPT_L[-1] <= OPT_C[-1]:
        secuencia_localizaciones[-1] = "londres"
    else:
        secuencia_localizaciones[-1] = "california"
    
    i = n-1
    while i > 0:
        if secuencia_localizaciones[i] == "londres":
            if OPT_L[i] == OPT_L[i-1] + arreglo_L[i]:
                secuencia_localizaciones[i-1] = "londres"
            else:
                secuencia_localizaciones[i-1] = "california"
        else:
            if OPT_C[i] == OPT_C[i-1] + arreglo_C[i]:
                secuencia_localizaciones[i-1] = "california"
            else:
                secuencia_localizaciones[i-1] = "londres"
        i -= 1

    return secuencia_localizaciones

print(plan_operativo3)