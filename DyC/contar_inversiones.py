def contar_inversiones(A, B):
    if len(arr) <= 1:
        return arr
    medio = len(arr) // 2
    izq, der = arr[:medio], arr[medio:]
    izq = merge_sort(izq)
    der = merge_sort(der)
    return merge(izq, der)

def merge(l1, l2):
    i, j = 0, 0
    res = []

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    res += l1[i:]
    res += l2[j:]
    return res