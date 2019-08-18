from unittest import TestCase
from numpy import array_equal

from matroids.algorithms import representative_family


class TestRepresentativeSets(TestCase):
    def test_wrong_family(self):
        family = [{1, 2}, {3, 4, 5}, {6}]
        with self.assertRaises(ValueError):
            representative_family(family, 2, 1)

    def test_empty_family(self):
        family = []
        result = representative_family(family, 2, 1)
        array_equal(result, [])

    def test_small_intersecting_family(self):
        family = [{'a', 'b'}, {'c', 'd'}, {'b', 'c'}, {'a', 'c'}, {'a', 'd'}]
        result = representative_family(family, 2, 1)
        correct_result = [{'a', 'b'}, {'b', 'c'}]
        self.assertTrue(all(s in result for s in correct_result), "Wrong answer was returned")
        self.assertEqual(len(result), 3, "Result is too big")
