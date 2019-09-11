from time import time   

class Sort:

    def BubleSort (self, lista):
        
        n = len(lista)
        for i in range (1, n):
            for j in range (n-1):
                if lista [j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
    t0 = time()
    BubleSort(lista)
    t1 = time()
    print ("lista ordenada ")
    print (lista, "\n")
    print ("tiempo (0:f) seg {0:f}".format(t1 - t0))
    
