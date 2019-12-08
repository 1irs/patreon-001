import unittest

from bubble_sort import bubble_sort


class BubbleSortTest(unittest.TestCase):

    def test(self):
        self.assertEqual(
            bubble_sort([3, 2, 1]),
            [1, 2, 3]
        )

    def test_empty(self):
        self.assertEqual(
            bubble_sort([]),
            []
        )

    def test_right_order(self):
        self.assertEqual(
            bubble_sort([1, 2, 3, 4]),
            [1, 2, 3, 4]
        )

    def test_float(self):
        self.assertEqual(
            bubble_sort([3.0, 6.0, 4.0, 5.0]),
            [3.0, 4.0, 5.0, 6.0]
        )

    def test_char(self):
        self.assertEqual(
            bubble_sort(['d', 't', 'a', 'h']),
            ['a', 'd', 'h', 't']
        )
