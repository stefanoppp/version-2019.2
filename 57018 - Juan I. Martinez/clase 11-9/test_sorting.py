import unittest
from sorting import Sort


class Test_sorting(unittest.TestCase):
    def test_bubble_1(self):
        self.bubble = Sort()
        self.array = [64, 34, 25, 12, 24, 11, 90]
        self.ordered = [11, 12, 24, 25, 34, 64, 90]
        self.assertEquals(self.bubble.bubbleSort(self.array), self.ordered)


if __name__ == '__main__':
    unittest.main()
