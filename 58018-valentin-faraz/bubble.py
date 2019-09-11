from time import time
def BubbleSort (lista):
    n = len(lista)
    i=0
    for i in range (1, n):
        for j in range (n-1):
            if lista [j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
t0 = time()
BubbleSort(lista)
t1 = time()
print ("lista ordenada ")
print (lista, "\n")
print ("tiempo {0:f} segundos".format(t1 - t0))