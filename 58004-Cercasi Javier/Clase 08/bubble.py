from time import time


def BubbleSort(lista):

    global comparaciones
    n = len(lista)
    i = 0

    for i in range(1, n):
        for j in range(n-1):
            comparaciones += 1

            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
comparaciones = 0
t0 = time()
t1 = time()

BubbleSort(lista)

print("lista ordenada ")
print(lista, "\n")
print("tiempo {0:f} segundos".format(t1 - t0))
print("comparacion ", comparaciones)