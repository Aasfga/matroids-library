from functools import reduce
from itertools import combinations
from typing import List, Set, Union

from . import representative_family


def kernel_hitting_set(family: List[Set], universe: Set, d: int, k: int) -> (List[Set], Set):
    if any(not s.issubset(universe) for s in family):
        raise ValueError("Wrong universe was provided")
    if any(len(s) != d for s in family):
        raise ValueError(f"There is set in family with size not equal to {d}")
    representation = representative_family(family, d, k)
    return representation, reduce(set.union, representation, set())


def brute_hitting_set(family: List[Set], universe: Set, k: int) -> Union[Set, None]:
    try:
        return next(
            set(subset) for subset in combinations(universe, k) if not any(s.isdisjoint(subset) for s in family))
    except StopIteration:
        return None
