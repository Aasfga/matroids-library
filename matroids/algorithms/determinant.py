from functools import reduce
from numpy import ndarray
from sympy import GF
from .gaussian_elimination import gaussian_elimination


def determinant(matrix: ndarray, field: GF):
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Square matrix must be provided")
    size = matrix.shape[0]
    matrix, swaps = gaussian_elimination(matrix, field)
    diagonal = [matrix[i, i] for i in range(size)]
    return reduce(field.mul, diagonal, field.one) * (field.one if swaps % 2 == 0 else -field.one)
