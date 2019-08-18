from functools import reduce
from itertools import combinations
from unittest import TestCase
from matroids.algorithms import kernel_set_packing, brute_set_packing


class TestSetPacking(TestCase):
    def test_empty_family(self):
        family = []
        result = kernel_set_packing(family, set(), 5, 2)
        self.assertEqual(result[0], [])
        self.assertEqual(result[1], set())

    def test_family_error(self):
        with self.assertRaises(ValueError):
            kernel_set_packing([{'a'}, {'a', 'b'}], {'a', 'b'}, 2, 1)

    def test_universe_error(self):
        with self.assertRaises(ValueError):
            kernel_set_packing([{1, 3}], {2}, 2, 1)

    def test_brute_small_family(self):
        family = [
            {1, 2, 3},
            {2, 3, 4},
            {4, 5, 6},
            {5, 6, 7},
            {1, 4, 6},
            {3, 5, 7},
            {10, 11, 12}
        ]
        universe = set(range(13))
        result = brute_set_packing(family, universe, 3)
        self.assertEqual(len(result), 3)
        union = reduce(set.union, result, set())
        self.assertEqual(len(union), 9)

    def test_brute_kernel(self):
        family = [{i, i + 1, i + 2, i + 3} for i in range(100)]
        universe = reduce(set.union, family, set())
        kernel = kernel_set_packing(family, universe, 4, 2)
        b_result = brute_set_packing(family, universe, 2)
        k_result = brute_set_packing(kernel[0], kernel[1], 2)
        self.assertEqual(len(b_result), 2)
        self.assertEqual(len(k_result), 2)
        b_elements = reduce(set.intersection, b_result, universe)
        k_elements = reduce(set.intersection, k_result, universe)
        self.assertEqual(len(b_elements), 0)
        self.assertEqual(len(k_elements), 0)

    def test_no_solution(self):
        family = [{1, 2, 3}, {1, 4, 5}, {1, 6, 7}, {1, 8, 9}]
        universe = {i for i in range(10)}
        result = brute_set_packing(family, universe, 2)
        self.assertIsNone(result)
