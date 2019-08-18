from typing import Set
from numpy import ndarray


class Matroid:
    def is_independent(self, s: Set) -> bool:
        raise NotImplementedError

    @property
    def rank(self) -> int:
        raise NotImplementedError

    @property
    def matrix(self) -> ndarray:
        raise NotImplementedError
