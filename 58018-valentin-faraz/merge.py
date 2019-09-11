#Para comparar con el Algoritmo de Mezcla (merge)
from time import time
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
    lista_nueva = []
    a = 0
    b = 0
    while a < len(listaA) and b < len(listaB):
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
lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
t0 = time()
lista = mergeSort(lista)
t1 = time()
print ("Lista ordenada:")
print (lista, "\n")
print ("Tiempo: {0:f} segundos".format(t1 - t0))