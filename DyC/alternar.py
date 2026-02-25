def alternar(arr):
    return _alternar(arr, 0, len(arr))

def _alternar(arr, ini, fin):
    if fin - ini == 2:
        return arr
    arr[1] == arr[len(arr) // 2]
    medio = ini + (fin - ini) // 2
    return _alternar(arr, ini, medio)

lista = [1,3,5,7,9,11,13,15,2,4,6,8,10,12,14,16]

def alterno(arr):
    arr[1], arr[len(arr) // 2] = arr[len(arr) // 2], arr[1]
    arr[2], arr[len(arr) // 2] = arr[len(arr) // 2], arr[2]
    arr[3], arr[len(arr) // 2 + 1] = arr[len(arr) // 2 + 1], arr[3]
    arr[4], arr[len(arr) // 2 ] = arr[len(arr) // 2], arr[4]
    arr[5], arr[len(arr) // 2] = arr[len(arr) // 2], arr[5]
    return arr

print(alterno(lista))