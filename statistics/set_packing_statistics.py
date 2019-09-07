from statistics.problem_runner import problem_runner
from matroids.algorithms import kernel_set_packing

parameters = [
    (4, 2, 1),
    (7, 3, 2),
    (15, 2, 3),
    (15, 2, 4),
    (10, 3, 2),
    (20, 3, 2),
    (10, 4, 2),
    (17, 3, 4),
    (11, 5, 2),
    (20, 4, 2)
]

for i, values in enumerate(parameters):
    n, d, k = values
    print("-----------------------------")
    print(f"Set Packing - Example {i + 1}")
    total_count, kernel_size = problem_runner(n, d, k, kernel_set_packing)
    print(f"n={n} d={d}, k={k}")
    print(f"total_count={total_count}")
    print(f"kernel_size={kernel_size}")
    print()
