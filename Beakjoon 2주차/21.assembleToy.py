import sys
from collections import deque


class DAG:
    def __init__(self, num_vertices: int):
        self.path = {i: [] for i in range(1, num_vertices + 1)}
        self.in_degree = [0] * num_vertices
        self.T = {i: 0 for i in range(1, num_vertices + 1)}
        self.T[num_vertices] = 1

    def add_edge(self, start: int, end: int, cost: int):
        self.path[start].append((end, cost))
        self.in_degree[end - 1] += 1


def bfs(g: DAG, size: int) -> None:
    tQue = deque()

    tQue.append(size)

    while tQue:
        tNow = tQue.popleft()
        nowCost = g.T[tNow]

        for tNext, nextCost in g.path[tNow]:
            g.T[tNext] += nextCost * nowCost
            g.in_degree[tNext - 1] -= 1

            if g.in_degree[tNext - 1] == 0:
                tQue.append(tNext)
    

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    g = DAG(N)

    for _ in range(M):
        X, Y, K = list(map(int, sys.stdin.readline().split()))
        g.add_edge(X, Y, K)
        
    bfs(g, N)

    for default_toy in g.path:
        if g.path[default_toy] == []:
            print(f"{default_toy} {g.T[default_toy]}")