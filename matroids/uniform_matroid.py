from typing import Set, Dict

from matroids.matroid import Matroid
from sympy import nextprime, Matrix
import numpy as np
from sympy.polys.domains import GF


class UniformMatroid(Matroid):
    @staticmethod
    def create_mapping(universe: Set, field: GF) -> Dict:
        mapping = zip(universe, range(1, len(universe) + 1))
        mapping = map(lambda x: (x[0], x[1] * field.one), mapping)
        return {u: field.one * x for u, x in mapping}

    def __init__(self, universe: Set, rank: int):
        self._rank: int = rank
        self.universe: Set = universe
        self.field = GF(nextprime(len(universe)))
        self.mapping: Dict = self.create_mapping(universe, self.field)

    def is_independent(self, s: Set) -> bool:
        if not s.issubset(self.universe):
            raise ValueError("Provided set is not subset of universe")
        return len(s) <= self.rank

    @property
    def rank(self) -> int:
        return self._rank

    @property
    def matrix(self):
        elems = self.mapping.values()
        matrix = [[elem ** i for i in range(self.rank)] for elem in elems]
        return np.array(matrix, dtype='object')
