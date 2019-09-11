import unittest
from sorting import Sort

class TestSorting(unittest.TestCase):

    def setUp(self):
        self.ls = Sort()
    def test_BubbleSort_comun(self):
        lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
        self.lista_ordenada = [0, 5, 9, 16, 21, 36, 40, 66, 71, 73]
        ans = self.ls.bubblesort(lista)
        self.assertEqual(ans,self.lista_ordenada)
    def test_BubbleSort_ordenada(self):
        lista = [0, 5, 9, 16, 21, 36, 40, 66, 71, 73]
        self.lista_ordenada = [0, 5, 9, 16, 21, 36, 40, 66, 71, 73]
        ans = self.ls.bubblesort(lista)
        self.assertEqual(ans,self.lista_ordenada)
    def test_BubbleSort_todos_numeros_iguales(self):
        lista = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        self.lista_ordenada = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ans = self.ls.bubblesort(lista)
        self.assertEqual(ans,self.lista_ordenada)
    def test_BubbleSort_con_numeros_negativos(self):
        lista = [0, 5, 9, 16, 21, -36, -40, 66, 71, 73]
        self.lista_ordenada = [-40, -36, 0, 5, 9, 16, 21, 66, 71, 73]
        ans = self.ls.bubblesort(lista)
        self.assertEqual(ans,self.lista_ordenada)

if __name__ == "__main__":
    unittest.main()