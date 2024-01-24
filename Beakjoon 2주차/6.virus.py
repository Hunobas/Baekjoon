import sys

class Graph:
    def __init__(self, num_vertices: int):
        self.path = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u: int, v: int):
        self.path[u].append(v)
        self.path[v].append(u)

    
def dfs(g:Graph, start: int, visited: set = None) -> set:
    if start not in g.path:
        return None
    if visited is None:
        visited = set()

    visited.add(start)

    for next in g.path[start]:
        if next not in visited:
            dfs(g, next, visited)
    
    return visited


if __name__ == "__main__":
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    g = Graph(V)

    for _ in range(E):
        A, B = list(map(int, sys.stdin.readline().split()))
        g.add_edge(A, B)
    
    print(len(dfs(g, 1)) - 1)