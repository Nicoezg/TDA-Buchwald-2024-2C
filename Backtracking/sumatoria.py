def sumatorias_n(lista, n):
    res = []
    return subset_sum(lista, 0, n, res)

def subset_sum(L, index, n, solucion_parcial):
	# Si encuentro una solucion la devuelvo
	if sum(solucion_parcial) == n:
		return [solucion_parcial]
	
	# Si por esta rama me paso, dejo de probar
	if sum(solucion_parcial) > n or index >= len(L):
		return []

	soluciones = []
	soluciones  += subset_sum(L, index+1, n, solucion_parcial + [L[index]])
	soluciones += subset_sum(L, index+1, n, solucion_parcial)

	return soluciones

print(sumatorias_n([1,2,3,4,5,6,8,9], 12))