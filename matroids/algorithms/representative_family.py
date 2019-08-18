import numpy as np
from numpy import array, ndarray
from functools import reduce
from typing import Set, List
from itertools import combinations
from sympy import GF
from uniform_matroid import UniformMatroid
from . import determinant
from . import gaussian_elimination


def _size_check(family: List[Set], size: int):
    return all(len(x) == size for x in family)


def _create_vectors(indexes: List[List[int]], p, q, matroid):
    vectors = []
    matrix = matroid.matrix
    for s in indexes:
        subsets = [list(x) for x in combinations(range(p + q), p)]
        vector = [determinant(matrix[i][:, s], matroid.field) for i in subsets]
        vectors.append(vector)
    return array(vectors).transpose()


def _representation_indexes(vectors: ndarray, field: GF):
    y, x = 0, 0
    height, width = vectors.shape
    indexes = []
    while y < height and x < width:
        while x < width and vectors[y][x] == field.zero:
            x += 1
        if x == width:
            break
        indexes.append(x)
        x += 1
        y += 1
    return indexes


def representative_family(family: List[Set], p, q) -> List[Set]:
    if not _size_check(family, p):
        raise ValueError(f"Not all sets in family have size {p}")
    if len(family) == 0:
        return []
    universe = reduce(set.union, family, set())
    matroid = UniformMatroid(universe, p + q)
    mapping = matroid.mapping
    index_family = [[mapping[x] for x in s] for s in family]
    vectors = _create_vectors(index_family, p, q, matroid)
    vectors, _ = gaussian_elimination(vectors, matroid.field)
    return [family[i] for i in _representation_indexes(vectors, matroid.field)]
