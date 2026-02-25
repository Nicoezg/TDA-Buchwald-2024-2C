def sortSecond(val):
    return val[1]

def sortFirst(val):
    return val[0]

def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def construir_rx(px, mediana):
    res = []
    for i in range(mediana, len(px)):
        res.append(px[i])
    return res

def construir_qx(px, mediana):
    res = []
    for i in range(0, mediana):
        res.append(px[i])
    return res

def construir_ry(py, mediana):
    res = []
    for punto in py:
        if punto[0] > mediana:
            res.append(punto)
    return res

def construir_qy(py, mediana):
    res = []
    for punto in py:
        if punto[0] <= mediana:
            res.append(punto)
    return res

def construir_s(py, d, x_max):
    res = []
    for punto in py:
        if dist(punto, (x_max, punto[1])) < d:
            res.append(punto)
    return res

def pareja_sy(sy):
    dist_min = -1
    pareja_min = [(0, 0), (0, 0)]
    for i in range(len(sy)):
        for j in range(i+1, i+15):
            if j >= len(sy):
                break
            dist_act = dist(sy[i], sy[j])
            if dist_min == -1 or dist_act < dist_min:
                pareja_min = [sy[i], sy[j]]
                dist_min = dist_act
    return pareja_min

def puntos_mas_cercanos(puntos):
    px = sorted(puntos, key = sortFirst)
    py = sorted(puntos, key = sortSecond)
    p0, p1 = puntos_mas_cercanos_rec(px, py)
    return p0, p1

def puntos_mas_cercanos_rec(px, py):
    if len(px) <= 3:
        if len(px) == 2:
            return px[0], px[1]
        d1 = dist(px[0], px[1])
        d2 = dist(px[0], px[2])
        d3 = dist(px[1], px[2])
        if d1 <= d2 and d1 <= d3:
            return px[0], px[1]
        if d2 <= d1 and d2 <= d3:
            return px[0], px[2]
        return px[1], px[2]
    mediana = len(px) // 2
    mediana_x = px[mediana][0]


    qx = construir_qx(px, mediana)
    rx = construir_rx(px, mediana)
    qy = construir_qy(py, mediana_x)
    ry = construir_ry(py, mediana_x)

    q0, q1 = puntos_mas_cercanos_rec(qx, qy)
    r0, r1 = puntos_mas_cercanos_rec(rx, ry)


    d = min(dist(q0, q1), dist(r0, r1))
    x_max = qx[-1][0]
    s = construir_s(py, d, x_max)
    s1, s2 = pareja_sy(s)
    
    
    if dist(s1, s2) != 0 and dist(s1, s2) < d: 
        return s1, s2
    if dist(q0, q1) < dist(r0, r1): 
        return q0, q1
    return r0, r1
puntos = [(7, 15), (25, 42), (3, 1), (50, 20), (19, 36), (10, 5), (65, 22), (13, 40), 
          (29, 11), (38, 50), (45, 32), (21, 47), (55, 19), (12, 30), (33, 14), (60, 25), (27, 38), (8, 18)]

def distancia_minima(p):
    dist_min = 0
    pareja_act = []
    for i in range(0, len(puntos)):
        for j in range(i + 1, len(puntos)):
            dist_act = dist(p[i], p[j])
            if dist_act < dist_min or dist_min == 0:
                dist_min = dist_act
                pareja_act = [p[i], p[j]]
    return pareja_act

print(distancia_minima(puntos))
print(puntos_mas_cercanos(puntos)) # (7,15) , (8, 18)
