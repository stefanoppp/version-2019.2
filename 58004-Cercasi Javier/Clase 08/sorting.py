class Sort (object):

    def __init__(self):
        self.working = False

    def BubbleSort(self, lista):
        n = len(lista)
        i = 0
        c = 0

        for i in range(1, n):
            for j in range(n-1):
                c += 1

                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j] 
        return (lista)

    def Insertionsort(self, lista):
        n = len(lista)
        i = 0

        for i in range(i, n):
            val = lista[i]
            j = i
            while j > 0 and lista[j-1] > val:

                lista[j] = lista[j-1]
                j -= 1
            lista[j] = val
        return (lista)
 
    def mergeSort(self, lista):
    
        if len(lista) <= 1:
            return lista

        medio = int(len(lista) / 2)
        izquierda = lista[:medio]
        derecha = lista[medio:]
        izquierda = self.mergeSort(izquierda)
        derecha = self.mergeSort(derecha)
        return self.merge(izquierda, derecha)

    def merge(self, listaA, listaB):

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

