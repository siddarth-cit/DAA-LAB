"""
Experiment 8
Travelling Salesman Problem using Branch and Bound
for Finding Optimal Path
"""

import copy
import heapq

INF = float("inf")


def reduce_matrix(matrix):
    """Reduce rows and columns and return the reduction cost."""
    mat = copy.deepcopy(matrix)
    n = len(mat)
    reduction_cost = 0

    # Row reduction
    for i in range(n):
        row_min = min(mat[i])

        if row_min != INF and row_min > 0:
            reduction_cost += row_min

            for j in range(n):
                if mat[i][j] != INF:
                    mat[i][j] -= row_min

    # Column reduction
    for j in range(n):
        col_min = min(mat[i][j] for i in range(n))

        if col_min != INF and col_min > 0:
            reduction_cost += col_min

            for i in range(n):
                if mat[i][j] != INF:
                    mat[i][j] -= col_min

    return mat, reduction_cost


def tsp_branch_and_bound(cost):
    n = len(cost)

    reduced, initial_bound = reduce_matrix(cost)

    # (bound, current_cost, path, reduced_matrix, visited)
    pq = [(initial_bound, 0, [0], reduced, {0})]

    best_cost = INF
    best_path = None

    while pq:
        bound, current_cost, path, matrix, visited = heapq.heappop(pq)

        if bound >= best_cost:
            continue

        if len(path) == n:
            total_cost = current_cost + cost[path[-1]][0]

            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path + [0]

            continue

        current = path[-1]

        for city in range(n):
            if city in visited or cost[current][city] == INF:
                continue

            new_cost = current_cost + cost[current][city]

            if new_cost >= best_cost:
                continue

            new_matrix = copy.deepcopy(matrix)

            for j in range(n):
                new_matrix[current][j] = INF

            for i in range(n):
                new_matrix[i][city] = INF

            new_matrix[city][0] = INF

            new_matrix, reduction = reduce_matrix(new_matrix)
            new_bound = new_cost + bound - (
                min(
                    x for x in matrix[current]
                    if x != INF
                )
                if any(x != INF for x in matrix[current])
                else 0
            ) + reduction

            if new_bound < best_cost:
                heapq.heappush(
                    pq,
                    (
                        new_bound,
                        new_cost,
                        path + [city],
                        new_matrix,
                        visited | {city},
                    ),
                )

    return best_path, best_cost


def main():
    cost = [
        [INF, 10, 8, 9, 7],
        [10, INF, 10, 5, 6],
        [8, 10, INF, 8, 9],
        [9, 5, 8, INF, 6],
        [7, 6, 9, 6, INF],
    ]

    cities = ["A", "B", "C", "D", "E"]

    print("5-City TSP - Cost Matrix:")
    print("     " + " ".join(f"{c:>5}" for c in cities))

    for i, row in enumerate(cost):
        values = [
            "INF" if value == INF else str(value)
            for value in row
        ]
        print(f"{cities[i]:>4} " +
              " ".join(f"{v:>5}" for v in values))

    best_path, best_cost = tsp_branch_and_bound(cost)

    print(
        "\nOptimal Tour:",
        " -> ".join(cities[i] for i in best_path)
    )
    print(f"Minimum Cost: {best_cost}")

    print("\nPath verification:")

    for i in range(len(best_path) - 1):
        u = best_path[i]
        v = best_path[i + 1]
        print(
            f" {cities[u]} -> {cities[v]}: "
            f"cost = {cost[u][v]}"
        )


if __name__ == "__main__":
    main()
