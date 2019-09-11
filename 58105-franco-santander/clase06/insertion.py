from time import time
def inserctionsort (lista) :
    i = 0
    n = len (lista)
    global comparaciones
    for i in range (1, n):
        val = lista [i]
        j = i
        while j > 0 and lista [j-1] > val:
            lista [j] = lista [j-1]
            j -= 1
            comparaciones += 1
        lista [j] = val

lista = [66, 71, 16, 21, 79, 9, 40, 60, 5]
comparaciones = 0
t0 = time()
inserctionsort(lista)
t1 = time()
print ("lista ordenada:")
print (lista, "\n")
print ("tiempo: {0:f} segundos".format (t1-t0))
print ("Comparaciones:", comparaciones)