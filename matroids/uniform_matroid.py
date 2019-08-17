from typing import Set
from matroids.matroid import Matroid
from sympy import nextprime, GF
from bidict import bidict
from numpy import array, ndarray


class UniformMatroid(Matroid):

    @staticmethod
    def _create_matrix(size: int, rank: int, field: GF) -> ndarray:
        values = [i * field.one for i in range(1, 1 + size)]
        matrix = [[value ** i for i in range(rank)] for value in values]
        return array(matrix, dtype='object').transpose()

    def __init__(self, universe: Set, rank: int):
        self.universe: frozenset = frozenset(universe)
        self._rank: int = rank
        self.field: GF = GF(nextprime(self.size))
        self.mapping: bidict = bidict({value: i for i, value in enumerate(universe)})
        self._matrix: ndarray = UniformMatroid._create_matrix(self.size, rank, self.field)

    def is_independent(self, s: Set) -> bool:
        if not s.issubset(self.universe):
            raise ValueError("Provided set is not subset of universe")
        return len(s) <= self.rank

    @property
    def rank(self) -> int:
        return self._rank

    @property
    def matrix(self):
        return self._matrix.copy()

    @property
    def size(self):
        return len(self.universe)
