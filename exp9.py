"""
Experiment 9
Efficient Bin Packing using Approximation Algorithms
"""

def first_fit(items, capacity=1.0):
    bins = []
    bin_contents = []

    for item in items:
        placed = False

        for i, space in enumerate(bins):
            if space >= item:
                bins[i] -= item
                bin_contents[i].append(item)
                placed = True
                break

        if not placed:
            bins.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


def first_fit_decreasing(items, capacity=1.0):
    return first_fit(sorted(items, reverse=True), capacity)


def best_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)

    bins = []
    bin_contents = []

    for item in sorted_items:
        best_index = -1
        best_space = float("inf")

        for i, space in enumerate(bins):
            remaining = space - item

            if space >= item and remaining < best_space:
                best_space = remaining
                best_index = i

        if best_index >= 0:
            bins[best_index] -= item
            bin_contents[best_index].append(item)
        else:
            bins.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


def display_bins(label, bins):
    print(f"\n{label}: {len(bins)} bins")

    for i, contents in enumerate(bins, 1):
        used = sum(contents)
        bar = "#" * int(used * 20)

        print(
            f" Bin {i}: "
            f"{[round(x, 1) for x in contents]} | "
            f"Used: {used:.1f} [{bar:<20}]"
        )


def main():
    items = [
        0.5, 0.7, 0.3, 0.9, 0.2,
        0.6, 0.8, 0.4, 0.1, 0.5
    ]

    capacity = 1.0
    lower_bound = int(
        -(-sum(items) // capacity)
    )

    print(f"Items: {items}")
    print(f"Capacity: {capacity}")
    print(f"Sum of items: {sum(items)}")
    print(f"Lower bound on bins: {lower_bound}")

    ff_bins = first_fit(items, capacity)
    ffd_bins = first_fit_decreasing(items, capacity)
    bfd_bins = best_fit_decreasing(items, capacity)

    display_bins("First Fit (FF)", ff_bins)
    display_bins("First Fit Decreasing (FFD)", ffd_bins)
    display_bins("Best Fit Decreasing (BFD)", bfd_bins)

    print(
        f"\nSummary: Lower Bound={lower_bound}, "
        f"FF={len(ff_bins)}, "
        f"FFD={len(ffd_bins)}, "
        f"BFD={len(bfd_bins)}"
    )


if __name__ == "__main__":
    main()
