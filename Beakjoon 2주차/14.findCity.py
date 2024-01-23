import sys
from collections import deque

class Graph:
    def __init__(self, num_vertices: int):
        self.path = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u: int, v: int):
        self.path[u].append(v)


def bfs_dijkstra(g: Graph, start: int, target: int) -> None:
    weights = {city: float('inf') for city in g.path}
    weights[start] = 0

    cQue = deque()
    cQue.appendleft(start)

    while cQue:
        cNow = cQue.popleft()

        for cNext in g.path[cNow]:
            if (total_weight := weights[cNow] + 1) < weights[cNext]:
                weights[cNext] = total_weight
                cQue.appendleft(cNext)

    result = 0
    for city, weight in weights.items():
        if weight == target:
            print(city)
            result += 1
    if not result:
        print(-1)


if __name__ == "__main__":
    N, M, K, X = list(map(int, sys.stdin.readline().split()))
    g = Graph(N)

    for _ in range(M):
        A, B = list(map(int, sys.stdin.readline().split()))
        g.add_edge(A, B)

    bfs_dijkstra(g, X, K)