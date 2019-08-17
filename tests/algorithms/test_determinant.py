from unittest import TestCase
from sympy import GF
from numpy import ndarray, array, vectorize

from matroids.algorithms import determinant


class TestDeterminant(TestCase):
    def determinant_comparer(self, matrix: ndarray, field: GF, correct_result: int):
        converter = vectorize(field)
        matrix = converter(matrix)
        correct_result = field(correct_result)
        result = determinant(matrix, field)
        self.assertEqual(result, correct_result, "Determinant is wrong")

    def test_1x1(self):
        field = GF(2)
        matrix = array([
            [1]
        ])
        self.determinant_comparer(matrix, field, 1)

    def test_1x2(self):
        field = GF(5)
        matrix = array([
            [1, 3]
        ])
        with self.assertRaises(ValueError):
            self.determinant_comparer(matrix, field, 3)

    def test_dependent_row(self):
        field = GF(5)
        matrix = array([
            [3, 4],
            [1, 3]
        ])
        self.determinant_comparer(matrix, field, 0)

    def test_dependent_column(self):
        field = GF(5)
        matrix = array([
            [1, 2],
            [4, 3]
        ])
        self.determinant_comparer(matrix, field, 0)

    def test_2x2(self):
        field = GF(11)
        matrix = array([
            [1, 2],
            [3, 4]
        ])
        self.determinant_comparer(matrix, field, 9)

    def test_3x3(self):
        field = GF(11)
        matrix = array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        self.determinant_comparer(matrix, field, 0)
