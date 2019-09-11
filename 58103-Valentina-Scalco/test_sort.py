import unittest
from sorting import sort
class Test_Bubble(unittest.TestCase):
    def test_bubble1(self):
        bubble = sort()   
        listamal =[66, 71, 16, 21, 79, 9, 40, 60, 5]
        listabien = bubble.bubbleSort(listamal)
        self.assertEqual(listamal, [5, 9, 16, 21, 40, 60, 66, 71, 79])
    def test_bubble_2(self):
        bubble = sort()
        listamal = [0, 1, 77, 3, 77, 4, 77, 3, 2, 5]
        listabien = bubble.bubbleSort(listamal)
        self.assertEqual(listabien, [0, 1, 2, 3, 3, 4, 5, 77, 77, 77])

       
if __name__ == "__main__":
    unittest.main()

 #t0 = time()
    #    bubbleSort(self)
  #      t1 = time()
   #     print ("lista ordenada: {} \n\n".format(lista))
     #   print (lista, "\n")
      #  print ("tiempo: {} segundos\n".format (t1-t0))
       # print ("comparaciones: {}".format (comparaciones))