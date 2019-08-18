from functools import reduce
from itertools import combinations
from typing import Set, List, Iterable, Union

from . import representative_family


def kernel_set_packing(family: List[Set], universe: Set, d: int, k: int) -> (List[Set], Set):
    if any(not s.issubset(universe) for s in family):
        raise ValueError("Wrong universe was provided")
    if any(len(s) != d for s in family):
        raise ValueError(f"There is set in family with size not equal to {d}")
    representation = representative_family(family, d, (k - 1) * d)
    return representation, reduce(set.union, representation, set())


def _is_correct_solution(sets: Iterable[Set]) -> bool:
    universe = reduce(set.union, sets, set())
    return len(universe) == sum(len(s) for s in sets)


def brute_set_packing(family: List[Set], universe: Set, k: int) -> Union[List, None]:
    if any(not s.issubset(universe) for s in family):
        raise ValueError("Wrong universe provided")
    try:
        return next(list(sets) for sets in combinations(family, k) if _is_correct_solution(sets))
    except StopIteration:
        return None
