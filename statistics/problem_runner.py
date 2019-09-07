import cProfile
from functools import reduce
from itertools import combinations

from statistics.analyzer import analyze_profiler


def problem_runner(n: int, d: int, k: int, algorithm):
    family = combinations(range(n), d)
    family = map(set, family)
    family = list(family)
    universe = reduce(set.union, family, set())
    profiler = cProfile.Profile()
    profiler.enable(builtins=False)

    kernel, _ = algorithm(family, universe, d, k)

    profiler.disable()

    stats = analyze_profiler(profiler)
    total_count = stats['total_count']
    return total_count, len(kernel)
