from time import time
def BubleSort (lista):
    global comparaciones
    n = len(lista)
    for i in range (1, n):  
        for j in range (n-1):
            comparaciones += 1
            if lista [j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def InsertionSort(lista):
    n = len(lista)
    global comparaciones
    for i in range(1, n):
        val = lista[i]
        j = i
        while j > 0 and lista[j-1] > val:
            lista[j] = lista[j-1]
            j -= 1
            comparaciones += 1
        lista[j] = val
    return lista

def mergeSort(lista):
    if len(lista) <= 1:
        return lista
    medio = int(len(lista) / 2)
    izquierda = lista[:medio]
    derecha = lista[medio:]
    izquierda = mergeSort(izquierda)
    derecha = mergeSort(derecha)
    return merge(izquierda, derecha)

def merge(listaA, listaB):
    global comparaciones
    lista_nueva = []
    a = 0
    b = 0
    while a < len(listaA) and b < len(listaB):
        comparaciones += 1
        if listaA[a] < listaB[b]:
            lista_nueva.append(listaA[a])
            a += 1
        else:
            lista_nueva.append(listaB[b])
            b += 1
    while a < len(listaA):
        lista_nueva.append(listaA[a])
        a += 1
    while b < len(listaB):
        lista_nueva.append(listaB[b])
        b += 1
    return lista_nueva

lista = [66, 71, 16, 21, 79, 9, 40, 60, 5]

comparaciones = 0
t0 = time()
#lista = InsertionSort(lista)
#lista = BubleSort(lista)
lista = mergeSort(lista)
t1 = time()
print("Lista ordenada: {} \n\n".format(lista))
print("Tiempo: {} segundos\n".format(t1 - t0))
print("Numero de comparaciones: {}".format(comparaciones))

