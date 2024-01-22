import sys

class Graph:
    def __init__(self, num_vertices: int):
        self.path = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u: int, v: int):
        self.path[u].append(v)
        self.path[v].append(u)


def dfs_isBinaryGraph(g: Graph, start: int, depth: int, visited: dict = None) -> bool:
    if visited is None:
        visited = {}

    result = True

    if depth % 2 == 0:
        visited[start] = 1
    else:
        visited[start] = -1

    for next in g.path[start]:
        if next not in visited:
            pre_result = result and dfs_isBinaryGraph(g, next, depth+1, visited)
        else:
            if depth % 2 == 0 and visited[next] == 1:
                return False
            elif depth % 2 == 1 and visited[next] == -1:
                return False
            else:
                return True
    
    return pre_result and result
            

if __name__ == "__main__":
    K = int(sys.stdin.readline())

    for _ in range(K):
        V, E = list(map(int, sys.stdin.readline().split()))
        g = Graph(V)

        for _ in range(E):
            A, B = list(map(int, sys.stdin.readline().split()))
            g.add_edge(A, B)

        if dfs_isBinaryGraph(g, 1, 0):
            print("YES")
        else:
            print("NO")
        