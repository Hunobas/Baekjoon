import sys
sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self, num_vertices: int):
        self.path = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u: int, v: int):
        self.path[u].append(v)
        self.path[v].append(u)


def dfs(g: Graph, start: int, whosParent: list[int], visited: list[int] = None) -> None:
    if visited is None:
        visited = set()

    visited.add(start)

    for next in g.path[start]:
        if next not in visited:
            whosParent[next - 1] = start
            dfs(g, next, whosParent, visited)


if __name__ == "__main__":
    V = int(sys.stdin.readline())
    E = V - 1
    g = Graph(V)
    whosParent = [0] * V

    for _ in range(E):
        A, B = list(map(int, sys.stdin.readline().split()))
        g.add_edge(A, B)
    
    dfs(g, 1, whosParent)

    for parent in whosParent[1:]:
        print(parent)