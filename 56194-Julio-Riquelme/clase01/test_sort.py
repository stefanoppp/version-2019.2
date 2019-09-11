import unittest
from sorting import Sort


class TestBubble(unittest.TestCase):

    def test_bubble_1(self):
        bubble = Sort()   
        listaDesordenada = [86, 17, 13, 22, 93, 23, 1, 67, 36, ]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_bubble_2(self):
        bubble = Sort()
        listaDesordenada = [0, 65, 92, 99, 76, 46, 45, 9, 5, 3]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 3, 5, 9, 45, 46, 65, 76, 92, 99])

    def test_bubble_3(self):
        bubble = Sort()
        listaDesordenada = [0, 23, 27, 33, 85, 25, 63, 77, 71]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 23, 25, 27, 33, 63, 71, 77, 85])


class Testinsertion(unittest.TestCase):

    def test_insertion_1(self):
        bubble = Sort()   
        listaDesordenada = [86, 17, 13, 22, 93, 23, 1, 67, 36, ]
        listaOrdenada = bubble.insertionSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_insertion_2(self):
        bubble = Sort()
        listaDesordenada = [0, 65, 92, 99, 76, 46, 45, 9, 5, 3]
        listaOrdenada = bubble.insertionSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 3, 5, 9, 45, 46, 65, 76, 92, 99])

    def test_insertion_3(self):
        bubble = Sort()
        listaDesordenada = [0, 23, 27, 33, 85, 25, 63, 77, 71]
        listaOrdenada = bubble.insertionSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 23, 25, 27, 33, 63, 71, 77, 85])


if __name__ == "__main__":
    unittest.main()
