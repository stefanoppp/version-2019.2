import unittest

from sorting import Sort


class TestBubble(unittest.TestCase):
    def test_Bubble_1(self):
        bubble = Sort()
        listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_Bubble_2(self):
        bubble = Sort()
        listaDesordenada = [1, -2, 3, -4, 5]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [-4, -2, 1, 3, 5])

    def test_Bubble_3(self):
        bubble = Sort()
        listaDesordenada = [1, 2, 3, 4, 5]
        listaOrdenada = bubble.BubbleSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [1, 2, 3, 4, 5])

    def test_Insertion_1(self):
        insertion = Sort()
        listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
        listaOrdenada = insertion.InsertionSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_Insertion_2(self):
        insertion = Sort()
        listaDesordenada = [1, -2, 3, -4, 5]
        listaOrdenada = insertion.InsertionSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [-4, -2, 1, 3, 5])

    def test_Insertion_3(self):
        insertion = Sort()
        listaDesordenada = [1, 2, 3, 4, 5]
        listaOrdenada = insertion.InsertionSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [1, 2, 3, 4, 5])

    def test_Merge_1(self):
        merge = Sort()
        listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
        listaOrdenada = merge.MergeSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [0, 5, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_Merge_2(self):
        merge = Sort()
        listaDesordenada = [1, -2, 3, -4, 5]
        listaOrdenada = merge.MergeSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [-4, -2, 1, 3, 5])

    def test_Merge_3(self):
        merge = Sort()
        listaDesordenada = [1, 2, 3, 4, 5]
        listaOrdenada = merge.MergeSort(listaDesordenada)
        self.assertEqual(listaOrdenada, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
