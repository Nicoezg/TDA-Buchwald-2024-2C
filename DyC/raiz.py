def raiz(funcion, a, b):
    p = (a + b) / 2 + a
    if funcion(p) == 0:
        return p
    if (funcion(p) > 0 and funcion(a) > 0) or (funcion(p) < 0 and funcion(a) < 0):
        return raiz(funcion, p, b)
    return raiz(funcion, a, p)

def funcion(n):
    return n - 35

print(type())