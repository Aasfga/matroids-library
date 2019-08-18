from unittest import TestCase
from sympy import GF
from numpy import array, ndarray, vectorize
from numpy.testing import assert_array_equal

from matroids.algorithms import gaussian_elimination


class TestGaussianElimination(TestCase):

    def gaussian_comparer(self, matrix: ndarray, field: GF, correct_result: ndarray, correct_swaps: int):
        converter = vectorize(field)
        matrix = converter(matrix)
        correct_result = converter(correct_result)
        result, swaps = gaussian_elimination(matrix, field)
        assert_array_equal(result, correct_result, "Matrix error")
        self.assertEqual(swaps, correct_swaps, "Swap error")

    def test_copy(self):
        field = GF(5)
        matrix = array([
            [1, 2],
            [2, 3]
        ])
        matrix_copy = matrix.copy()
        gaussian_elimination(matrix, field)
        assert_array_equal(matrix, matrix_copy, "Matrix hasn't been copied")

    def test_2x2(self):
        field = GF(7)
        matrix = array([
            [1, 2],
            [4, 5]
        ])
        correct_result = array([
            [4, 5],
            [0, 6]
        ])
        self.gaussian_comparer(matrix, field, correct_result, 1)

    def test_3x3(self):
        field = GF(7)
        matrix = array([
            [6, 2, 3],
            [1, 4, 1],
            [2, 2, 5]
        ])
        correct_result = array([
            [6, 2, 3],
            [0, 6, 4],
            [0, 0, 0]
        ])
        self.gaussian_comparer(matrix, field, correct_result, 0)

    def test_3x4(self):
        field = GF(11)
        matrix = array([
            [1, 2, 3, 4],
            [3, 6, 9, 1],
            [2, 5, 4, 8]
        ])
        correct_result = array([
            [3, 6, 9, 1],
            [0, 1, 9, 0],
            [0, 0, 0, 0]
        ])
        self.gaussian_comparer(matrix, field, correct_result, 2)

    def test_5x5(self):
        field = GF(2)
        matrix = array([
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0]
        ])
        correct_result = array([
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]
        ])
        self.gaussian_comparer(matrix, field, correct_result, 2)
