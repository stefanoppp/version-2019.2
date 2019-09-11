class Sort():

    def BubbleSort(self, lista):
        n = len(lista)
        i = 0
        for i in range(1, n):
            for j in range(n-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista


class insertion():
    def insertionSort(lista):
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