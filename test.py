import unittest

from bubble_sort import bubble_sort


class BubbleSortTest(unittest.TestCase):

    def test(self):
        self.assertEqual(
            bubble_sort([3, 2, 1]),
            []
        )
