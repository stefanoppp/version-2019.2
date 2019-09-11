
import unittest
from sorting import Sort


class Test_sorting(unittest.TestCase):
    def test_bubble_1(self):
        self.bubble = Sort()
        self.array = [64, 34, 25, 12, 24, 11, 90]
        self.ordered = [11, 12, 24, 25, 34, 64, 90]
        self.assertEquals(self.bubble.bubbleSort(self.array), self.ordered)

    def test_bubble_2(self):
        self.bubble = Sort()
        self.array = [12, 11, 13, 5, 6]
        self.ordered = [5, 6, 11, 12, 13]
        self.assertEquals(self.bubble.bubbleSort(self.array), self.ordered)

    def test_insert_1(self):
        self.insert = Sort()
        self.array = [12, 11, 13, 5, 6]
        self.ordered = [5, 6, 11, 12, 13]
        self.assertEqual(self.insert.insertSort(self.array), self.ordered)

    def test_insert_2(self):
        self.insert = Sort()
        self.array = [64, 34, 25, 12, 24, 11, 90]
        self.ordered = [11, 12, 24, 25, 34, 64, 90]
        self.assertEqual(self.insert.insertSort(self.array), self.ordered)

    def test_merge_1(self):
        self.merge = Sort()
        self.array = [12, 11, 13, 5, 6, 7]
        self.ordered = [5, 6, 7, 11, 12, 13]
        self.assertEqual(self.merge.mergeSort(self.array), self.ordered)

    def test_merge_2(self):
        self.merge = Sort()
        self.array = [64, 34, 25, 12, 24, 11, 90]
        self.ordered = [11, 12, 24, 25, 34, 64, 90]
        self.assertEqual(self.merge.mergeSort(self.array), self.ordered)


if __name__ == '__main__':
    unittest.main()