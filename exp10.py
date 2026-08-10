"""
Experiment 10
Improving Quick Sort Efficiency using Randomized Algorithm
"""

import random
import sys
import time

sys.setrecursionlimit(20000)

comparisons = 0


def partition(arr, low, high):
    global comparisons

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        deterministic_quicksort(
            arr, low, pivot_index - 1
        )
        deterministic_quicksort(
            arr, pivot_index + 1, high
        )


def randomized_quicksort(arr, low, high):
    if low < high:
        random_index = random.randint(low, high)

        arr[random_index], arr[high] = (
            arr[high],
            arr[random_index]
        )

        pivot_index = partition(arr, low, high)

        randomized_quicksort(
            arr, low, pivot_index - 1
        )
        randomized_quicksort(
            arr, pivot_index + 1, high
        )


def run_test(sort_function, arr):
    global comparisons

    data = arr[:]
    comparisons = 0

    start = time.perf_counter()

    sort_function(data, 0, len(data) - 1)

    elapsed = (time.perf_counter() - start) * 1000

    return comparisons, elapsed


def main():
    n = 5000

    test_cases = {
        "Random": [
            random.randint(1, 100000)
            for _ in range(n)
        ],
        "Sorted": list(range(n)),
        "Reverse": list(range(n, 0, -1)),
        "Nearly Sorted": list(range(n)),
    }

    # Slightly shuffle the nearly sorted input.
    nearly_sorted = test_cases["Nearly Sorted"]

    for _ in range(n // 20):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        nearly_sorted[i], nearly_sorted[j] = (
            nearly_sorted[j],
            nearly_sorted[i],
        )

    print(
        f"{'Input Type':<16}"
        f"{'DQS Comps':>12}"
        f"{'DQS Time(ms)':>14}"
        f"{'RQS Comps':>12}"
        f"{'RQS Time(ms)':>14}"
    )

    print("-" * 72)

    for case, data in test_cases.items():
        d_comps, d_time = run_test(
            deterministic_quicksort, data
        )

        r_comps, r_time = run_test(
            randomized_quicksort, data
        )

        print(
            f"{case:<16}"
            f"{d_comps:>12}"
            f"{d_time:>14.2f}"
            f"{r_comps:>12}"
            f"{r_time:>14.2f}"
        )


if __name__ == "__main__":
    main()
