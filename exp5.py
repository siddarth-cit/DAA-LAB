"""
Experiment 5
Finding Min-Max Value using Divide and Conquer
"""

import random


comparison_count = 0


def min_max_dc(arr, low, high):
    global comparison_count

    # Base case: one element
    if low == high:
        return arr[low], arr[low]

    # Base case: two elements
    if high == low + 1:
        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]

        return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    left_min, left_max = min_max_dc(arr, low, mid)
    right_min, right_max = min_max_dc(arr, mid + 1, high)

    # Combine
    comparison_count += 1
    overall_min = left_min if left_min < right_min else right_min

    comparison_count += 1
    overall_max = left_max if left_max > right_max else right_max

    return overall_min, overall_max


def min_max_naive(arr):
    minimum = arr[0]
    maximum = arr[0]
    comparisons = 0

    for value in arr[1:]:
        comparisons += 1

        if value < minimum:
            minimum = value

        comparisons += 1

        if value > maximum:
            maximum = value

    return minimum, maximum, comparisons


def main():
    global comparison_count

    # Demonstration
    arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

    comparison_count = 0
    minimum, maximum = min_max_dc(
        arr, 0, len(arr) - 1
    )

    dc_comparisons = comparison_count
    _, _, naive_comparisons = min_max_naive(arr)

    print(f"Array: {arr}")
    print(f"Min: {minimum}, Max: {maximum}")
    print(f"D&C Comparisons: {dc_comparisons}")
    print(f"Naive Comparisons: {naive_comparisons}")

    print(
        f'\n{"Size":>8} '
        f'{"DC Comps":>12} '
        f'{"Naive Comps":>14} '
        f'{"Formula 3n/2-2":>16}'
    )
    print("-" * 56)

    for size in [10, 100, 1000, 10000]:
        data = [
            random.randint(1, 10000)
            for _ in range(size)
        ]

        comparison_count = 0

        min_max_dc(
            data, 0, len(data) - 1
        )

        dc = comparison_count
        _, _, naive = min_max_naive(data)
        formula = 3 * size // 2 - 2

        print(
            f"{size:>8} {dc:>12} "
            f"{naive:>14} {formula:>16}"
        )


if __name__ == "__main__":
    main()
