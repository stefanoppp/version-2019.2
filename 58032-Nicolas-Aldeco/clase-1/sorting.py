class Sort():

    def bubblesort(self,lista):
        n = len(lista)
        for i in range (1, n):
            for j in range (n-1):
                if lista [j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    def insertionsort(self,listx):
        n=len(listx)
        i = 0
        for i in range(i,n):
            vol = listx[i] 
            j = i
            while j>0 and listx [j-1]>vol:
                listx[j]=listx[j-1]
                j -= 1
            listx[j]=vol
        return listx