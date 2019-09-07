from statistics.problem_runner import problem_runner
from matroids.algorithms import kernel_hitting_set

parameters = [
    (3, 2, 1),
    (5, 2, 2),
    (30, 2, 1),
    (15, 3, 1),
    (10, 4, 2),
    (12, 7, 1),
    (20, 4, 2),
    (50, 3, 2),
    (25, 4, 2),
    (15, 5, 3)
]

for i, values in enumerate(parameters):
    n, d, k = values
    print("-----------------------------")
    print(f"Hitting Set - Example {i + 1}")
    total_count, kernel_size = problem_runner(n, d, k, kernel_hitting_set)
    print(f"n={n} d={d}, k={k}")
    print(f"total_count={total_count}")
    print(f"kernel_size={kernel_size}")
    print()
