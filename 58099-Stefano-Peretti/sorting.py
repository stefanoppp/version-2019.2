class Sort():

    def BubbleSort(self, lista):
        n = len(lista)
        for i in range(1, n):
            for j in range(n-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    def InsertionSort(self, lista):
        i = 0
        n = len(lista)
        for i in range(1, n):
            val = lista[i]
            j = i
            while j > 0 and lista[j-1] > val:
                lista[j] = lista[j-1]
                j -= 1
            lista[j] = val
        return lista

    def MergeSort(self, lista):
        if len(lista) <= 1:
            return lista

        medio = len(lista) / 2

        izquierda = lista[:int(medio)]

        derecha = lista[int(medio):]

        izquierda = self.MergeSort(izquierda)

        derecha = self.MergeSort(derecha)

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