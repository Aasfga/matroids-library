import numpy as np
from sympy import GF


def gaussian_elimination(matrix: np.ndarray, field: GF) -> (np.ndarray, int):
    matrix = matrix.copy()
    height, width = matrix.shape
    y, x = 0, 0
    swaps = 0
    while y < height and x < width:
        swap_index = y + np.argmax(matrix[y:, x])
        if matrix[swap_index][x] == field.zero:
            x += 1
            continue
        matrix[[y, swap_index]] = matrix[[swap_index, y]]
        swaps += 1 if y != swap_index else 0
        for i in range(y + 1, height):
            c = matrix[i, x] / matrix[y, x]
            for j in range(x, width):
                matrix[i][j] -= c * matrix[y, j]
        y += 1
        x += 1
    return matrix, swaps
