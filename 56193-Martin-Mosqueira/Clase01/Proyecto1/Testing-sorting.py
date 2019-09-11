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

class TestInsertionsort(unittest.TestCase):
    def test_insertionsort(self):
        bubble = Sort()  # clase que va a recibir cada uno de los ingresos,define el estado inicial
        listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
        listaOrdenada = bubble.insertionsort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])




if __name__ == "__main__":
   unittest.main()