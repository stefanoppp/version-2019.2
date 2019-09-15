import unittest
from sorting import sorting
class test_Bubble(unittest.TestCase):
    def test_bubble_0(self):
        bubble = sorting()   
        listamal =[66, 71, 16, 21, 79, 9, 40, 60, 5]
        listabien = bubble.bubbleSorting(listamal)
        self.assertEqual(listamal, [5, 9, 16, 21, 40, 60, 66, 71, 79])
    def test_bubble_1(self):
        bubble = sorting()
        listamal = [0, 1, 77, 3, 77, 4, 77, 3, 2, 5]
        listabien = bubble.bubbleSorting(listamal)
        self.assertEqual(listabien, [0, 1, 2, 3, 3, 4, 5, 77, 77, 77])
       
if __name__ == "__main__":
    unittest.main()