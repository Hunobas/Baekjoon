import sys
from heapq import heapify, heappop, heappush

class Graph:
    def __init__(self, num_vertices: int):
        self.path = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u: int, v: int, cost: int):
        self.path[u].append([cost, v])
        self.path[v].append([cost, u])


def prim(g: Graph, start_node: int, visited: list[bool]) -> int:
    visited[start_node - 1] = True
    neighbor = g.path[start_node]
    heapify(neighbor)
    total_weight = 0

    while neighbor:
        weight, v = heappop(neighbor)

        if visited[v - 1] == False:
            visited[v - 1] = True
            total_weight += weight

            for next_node in g.path[v]:
                if visited[next_node[1] - 1] == False:
                    heappush(neighbor, next_node)

    return total_weight


if __name__ == "__main__":
    V, E = list(map(int, sys.stdin.readline().split()))
    g = Graph(V)
    visited = [False] * V

    for _ in range(E):
        A, B, C = list(map(int, sys.stdin.readline().split()))
        g.add_edge(A, B, C)
    
    print(prim(g, 1, visited))