from typing import Set


class Matroid:
    def is_independent(self, s: Set) -> bool:
        raise NotImplementedError

    @property
    def rank(self) -> int:
        raise NotImplementedError

    @property
    def matrix(self):
        raise NotImplementedError


