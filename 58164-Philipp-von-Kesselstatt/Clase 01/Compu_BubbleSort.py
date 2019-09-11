from time import time


def BubleSort(lista):
    global comparaciones
    n = len(lista)
    for i in range(1, n):
        for j in range(n-1):
            comparaciones += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
comparaciones = 0
t0 = time()
BubleSort(lista)
t1 = time()
print("lista ordenada ")
print(lista, "\n")
print("tiempo {0:f} seg".format(t1 - t0))
print("comparacion ", comparaciones)
