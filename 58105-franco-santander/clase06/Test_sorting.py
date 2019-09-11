import unittest
from sorting import Sort
class TestBubble(unittest.TestCase):
   def test_bubble_1(self):
       bubble = Sort()    #clase que va a recibir cada uno de los ingresos,define el estado inicial
       listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
       listaOrdenada = bubble.BubbleSort(listaDesordenada)
       self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])
   def test_bubble_2(self):
       bubble = Sort()
       listaDesordenada = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
       listaOrdenada = bubble.BubbleSort(listaDesordenada)
       self.assertEqual(listaOrdenada, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
   
class TestInsertion(unittest.TestCase):
    def test_insertion_1(self):
        insertion = Sort()    #clase que va a recibir cada uno de los ingresos,define el estado inicial 
        listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
        listaOrdenada = insertion.InsertionSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])
    def test_insertion_2(self):
        insertion = Sort()
        listaDesordenada = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        listaOrdenada = insertion.InsertionSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    def test_insertion_3(self):
        insertion = Sort()
        listaDesordenada = [-2, -5, -99, 1, 5, 3, 1, 8, 1, -5]
        listaOrdenada = insertion.InsertionSort(listaDesordenada)
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
