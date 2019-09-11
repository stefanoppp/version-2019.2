import unittest
from sorting import Sort 

class TestSorting (unittest.TestCase):
    
    def test_Bubble_1(self):
       bubble = Sort()
       listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
       listaOrdenada = bubble.BubbleSort(listaDesordenada)
       self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_Bubble_2(self):
       bubble = Sort ()
       lista= [1, 1, 1, 1, 1, 1, 1, 1, 1 , 1]
       listaOrdenada = bubble.BubbleSort(lista)
       self.assertEqual(listaOrdenada, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    
    def test_InsertionSort_1(self):
       bubble = Sort()
       listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
       listaOrdenada = bubble.BubbleSort(listaDesordenada)
       self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_InsertionSort_2(self):
       bubble = Sort ()
       lista= [1, 1, 1, 1, 1, 1, 1, 1, 1 , 1]
       listaOrdenada = bubble.BubbleSort(lista)
       self.assertEqual(listaOrdenada, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    
    
    



if __name__ == "__main__":
    unittest.main()
