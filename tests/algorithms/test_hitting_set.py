from functools import reduce
from unittest import TestCase

from matroids.algorithms import kernel_hitting_set, brute_hitting_set


class TestHittingSet(TestCase):
    def test_empty_family(self):
        family = []
        result = kernel_hitting_set(family, set(), 5, 2)
        self.assertEqual(result[0], [])
        self.assertEqual(result[1], set())

    def test_family_error(self):
        family = [{'a', 'b'}, {'c', 'd', 'e'}]
        with self.assertRaises(ValueError):
            kernel_hitting_set(family, {'a', 'b', 'c', 'd', 'e'}, 2, 1)

    def test_universe_error(self):
        family = [{'a'}]
        with self.assertRaises(ValueError):
            kernel_hitting_set(family, {'b'}, 2, 1)

    def test_kernel_small_family(self):
        family = [{1, 2, 3}, {1, 3, 4}, {1, 2, 5}, {1, 8, 9}, {1, 5, 6}]
        universe = reduce(set.union, family, set())
        kernel, _ = kernel_hitting_set(family, universe, 3, 1)
        intersection = reduce(set.intersection, kernel, universe)
        self.assertEqual(intersection, {1})
        self.assertLessEqual(len(kernel), 3)

    def test_brute_small_family(self):
        family = [{1, 2, 3}, {1, 3, 4}, {1, 2, 5}, {1, 8, 9}, {1, 5, 6}]
        universe = reduce(set.union, family, set())
        result = brute_hitting_set(family, universe, 1)
        self.assertEqual(result, {1})

    def test_kernel_brute(self):
        family = [
            {1, 3}, {2, 4}, {1, 5}, {2, 6},
            {1, 7}, {2, 8}, {1, 9}, {2, 10},
            {1, 11}, {2, 12}, {1, 12}, {2, 11},
            {1, 10}, {2, 9}, {1, 8}, {2, 7}, {1, 6}
        ]
        universe = {i for i in range(13)}
        kernel = kernel_hitting_set(family, universe, 2, 2)
        k_result = brute_hitting_set(kernel[0], kernel[1], 2)
        b_result = brute_hitting_set(family, universe, 2)
        self.assertLessEqual(len(kernel[0]), 6)
        self.assertLessEqual(len(kernel[1]), 12)
        self.assertEqual(k_result, b_result)
        self.assertEqual(k_result, {1, 2})

    def test_no_solution(self):
        family = [{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}]
        universe = {i for i in range(7)}
        result = brute_hitting_set(family, universe, 1)
        self.assertIsNone(result)
