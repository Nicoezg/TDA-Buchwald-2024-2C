from grafo import Grafo

def hay_isomorfismo(g, f):
    if len(g) != len(f):
        return False
    return _hay_isomorfismo(g,f, list(g.obtener_vertices()),list(f.obtener_vertices()), 0 , 0, {})

def _hay_isomorfismo(g, f, vertices_g, vertices_f, i, j, res):
    if i == len(g):
        return True
    
    if j == len(f):
        return False
    
    v_f = vertices_f[i]
    v_g = vertices_g[j]

    if es_isomorfismo(g, f, v_g, v_f, res):
        if _hay_isomorfismo(g, f, vertices_g, vertices_f, i + 1, 0, res):
            return True
    del res[v_f]
    return _hay_isomorfismo(g, f, vertices_g, vertices_f, i, j + 1, res)

def es_isomorfismo(g, f, v_g, v_f, res):
    if v_f in res or v_g in res.values():
        res[v_f] = v_g
        return False
    res[v_f] = v_g
    return len(g.adyacentes(v_g)) == len(f.adyacentes(v_f))

            

grafo = Grafo(False, False, [1,2,3])
frafo = Grafo(False, False, ["a","b","c"])
grafo.agregar_arista(1,2)
grafo.agregar_arista(2,3)
frafo.agregar_arista("a", "b")
frafo.agregar_arista("b", "c")
frafo.agregar_arista("c", "a")
print(hay_isomorfismo(grafo, frafo))
