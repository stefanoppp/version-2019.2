import unittest
from sorting import (Sort)


class Test_Lista_Bubble(unittest.TestCase):

    def test_Bubble_1(self):
        bubble = Sort()
        listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_Bubble_2(self):
        bubble = Sort()
        listaDesordenada = [0, 5, 9, 16, 21, 36, 40, 66, 71, 73]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_Bubble_3(self):
        bubble = Sort()
        listaDesordenada = [-36, -71, -16, -21, -73, -9, -0, -40, -66, -5]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [-73, -71, -66, -40, -36, -21, -16, -9, -5, 0])

    def test_Bubble_4(self):
        bubble = Sort()
        listaDesordenada = [3, 4, 5, 5, 5, 8, 6, 1, 2, 3]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [1, 2, 3, 3, 4, 5, 5, 5, 6, 8])


class TestInsertion(unittest.TestCase):

    def test_insertion_1(self):
        insertion = Sort()    #clase que va a recibir cada uno de los ingresos,define el estado inicial 
        listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
        listaOrdenada = insertion.Insertionsort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_insertion_2(self):
        insertion = Sort()
        listaDesordenada = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        listaOrdenada = insertion.Insertionsort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    def test_insertion_3(self):
        insertion = Sort()
        listaDesordenada = [-2, -5, -99, 1, 5, 3, 1, 8, 1, -5]
        listaOrdenada = insertion.Insertionsort(listaDesordenada)
        self.assertEqual(listaOrdenada, [-99, -5, -5, -2, 1, 1, 1, 3, 5, 8])


class TestMerge(unittest.TestCase):

    def test_merge_1(self):

        merge = Sort()    #clase que va a recibir cada uno de los ingresos,define el estado inicial 
        listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
        listaOrdenada = merge.mergeSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_merge_2(self):

        merge = Sort()
        listaDesordenada = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        listaOrdenada = merge.mergeSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    def test_merge_3(self):
        merge = Sort()
        listaDesordenada = [-2, -5, -99, 1, 5, 3, 1, 8, 1, -5]
        listaOrdenada = merge.mergeSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [-99, -5, -5, -2, 1, 1, 1, 3, 5, 8])


if __name__ == "__main__":
    unittest.main()