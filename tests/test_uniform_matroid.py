import numpy as np
from unittest import TestCase
from uniform_matroid import UniformMatroid
from itertools import combinations
from numpy import array_equal


class TestUniformMatroid(TestCase):
    def setUp(self) -> None:
        self.size = 10
        self.universe = set(range(self.size))
        self.rank = 5
        self.matroid = UniformMatroid(self.universe, self.rank)

    def tearDown(self) -> None:
        self.universe = None
        self.rank = None
        self.matroid = None

    def test_rank(self):
        self.assertEqual(self.matroid.rank, self.rank)

    def test_size(self):
        self.assertEqual(self.matroid.size, len(self.universe))

    def test_matrix(self):
        matrix = self.matroid.matrix
        field = self.matroid.field
        self.assertEqual(matrix.shape, (self.rank, self.size), "Matrix has wrong shape")
        self.assertGreater(field.characteristic(), self.matroid.size, "Field isn't bigger than universe")
        unique_row = matrix[1]
        self.assertEqual(len(set(unique_row)), len(unique_row), "Unique field elements are not unique")
        self.assertFalse(np.any(matrix == field.zero), "Zero is in matrix")
        matrix[0][0] = field.zero
        new_matrix = self.matroid.matrix
        self.assertFalse(array_equal(matrix, new_matrix), "Matrix wasn't copied")

    def test_is_independent(self):
        s = set(next(combinations(self.universe, self.rank)))
        self.assertTrue(self.matroid.is_independent(s), "Independent set is dependent")
        s = set(next(combinations(self.universe, self.rank + 1)))
        self.assertFalse(self.matroid.is_independent(s), "Dependent set is independent")
        s = {'a', 'b', 'c', 'd'}
        with self.assertRaises(ValueError):
            self.matroid.is_independent(s)

    def test_mapping(self):
        mapping = self.matroid.mapping
        keys_checker = list(range(self.size))
        keys = list(mapping.keys())
        self.assertEqual(keys, keys_checker)
        values_checker = list(self.universe)
        values = list(mapping.values())
        self.assertEqual(values, values_checker)
