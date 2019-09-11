from time import time
def insertionsort (lista):
    n=len(lista)
    i=0
    for i in range(i,n):
        val = lista[i]
        j=i
        while j>0 and lista[j-1]>val:
            lista[j]=lista[j-1]
            j-=1
        lista[j]=val

lista=[66,71,16,21,79,9,40,60,5]
t0=time()
insertionsort(lista)
t1=time()
print ("lista ordenada:")
print (lista, "\n")
print ("Tiempo: {0:f} segundos".format(t1 - t0))

