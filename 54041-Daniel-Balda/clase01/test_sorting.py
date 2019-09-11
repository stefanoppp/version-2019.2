import unittest
from sorting import Sort, Insertion


class TestBubble(unittest.TestCase):

    def test_bubble_1(self):
        bubble = Sort()
        listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_bubble_2(self):
        bubble = Sort()
        listaDesordenada = [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 1, 2, 2, 4, 6, 8, 9, 23, 25])

    def test_bubble_3(self):
        bubble = Sort()
        listaDesordenada = [5, 0, 15, 25, 20, 35, 40, 25, 6, 9]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 6, 9, 15, 20, 25, 25, 35, 40])


class TestInsertion(unittest.TestCase):

    def test_insertion_1(self):
        bubble = Insertion()
        listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
        listaOrdenada = bubble.insertionsort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_insertion_2(self):
        bubble = Insertion()
        lista = [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
        listaOrdenada = bubble.insertionsort(lista)
        self.assertEqual(listaOrdenada, [0, 1, 2, 2, 4, 6, 8, 9, 23, 25])

    def test_insertion_3(self):
        bubble = Insertion()
        lista = [5, 0, 15, 25, 20, 35, 40, 25, 6, 9]
        listaOrdenada = bubble.insertionsort(lista)
        self.assertEqual(listaOrdenada, [0, 5, 6, 9, 15, 20, 25, 25, 35, 40])


if __name__ == "__main__":
    unittest.main()
