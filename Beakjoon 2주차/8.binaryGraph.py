import sys
sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self, num_vertices: int):
        self.path = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u: int, v: int):
        self.path[u].append(v)
        self.path[v].append(u)


def dfs_isBinaryGraph(g: Graph, start: int, depth: int, visited: dict) -> bool:
    result = True

    # 짝수번 노드에 파란색 칠 (1)
    if depth % 2 == 0:
        visited[start] = 1
    # 홀수번 노드에 빨간색 칠 (-1)
    else:
        visited[start] = -1

    for next in g.path[start]:
        if next not in visited:
            if not dfs_isBinaryGraph(g, next, depth+1, visited):
                return False
        else:
            if depth % 2 == 0 and visited[next] == 1:
                return False
            elif depth % 2 == 1 and visited[next] == -1:
                return False
    
    return result
            

if __name__ == "__main__":
    K = int(sys.stdin.readline())

    for _ in range(K):
        visited = {}
        V, E = list(map(int, sys.stdin.readline().split()))
        g = Graph(V)

        for _ in range(E):
            A, B = list(map(int, sys.stdin.readline().split()))
            g.add_edge(A, B)

        result = True

        for node in g.path:
            if node in visited:
                continue
            else:
                if not dfs_isBinaryGraph(g, node, 0, visited):
                    result = False
        
        if result:
            print("YES")
        else:
            print("NO")
        