"""
Experiment 3
Implementation of Kruskal's and Prim's Algorithms
for Minimum Spanning Tree
"""

import heapq


class UnionFind:

    def __init__(self, vertices):
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, x, y):

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True


def kruskal(vertices, edges):

    mst = []
    total_cost = 0

    uf = UnionFind(vertices)

    edges = sorted(edges)

    for weight, u, v in edges:

        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

        if len(mst) == vertices - 1:
            break

    return mst, total_cost


def prim(vertices, graph, start=0):

    visited = [False] * vertices

    pq = [(0, start, -1)]

    mst = []
    total_cost = 0

    while pq:

        weight, node, parent = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True

        if parent != -1:
            mst.append((parent, node, weight))
            total_cost += weight

        for neighbour, cost in graph[node]:
            if not visited[neighbour]:
                heapq.heappush(
                    pq,
                    (cost, neighbour, node)
                )

    return mst, total_cost


def build_graph(edges):

    graph = {}

    for weight, u, v in edges:

        graph.setdefault(u, []).append((v, weight))
        graph.setdefault(v, []).append((u, weight))

    return graph


def display(title, mst, cost):

    print(title)
    print("-" * len(title))

    for u, v, w in mst:
        print(f"{u} -- {v}  Weight = {w}")

    print(f"\nTotal MST Cost = {cost}\n")


def main():

    vertices = 7

    edges = [
        (7, 0, 1),
        (5, 0, 3),
        (8, 1, 2),
        (9, 1, 3),
        (7, 1, 4),
        (5, 2, 4),
        (15, 3, 4),
        (6, 3, 5),
        (8, 4, 5),
        (9, 4, 6),
        (11, 5, 6),
    ]

    graph = build_graph(edges)

    kruskal_mst, kruskal_cost = kruskal(vertices, edges)

    prim_mst, prim_cost = prim(vertices, graph)

    display("Kruskal's Algorithm", kruskal_mst, kruskal_cost)

    display("Prim's Algorithm", prim_mst, prim_cost)


if __name__ == "__main__":
    main()