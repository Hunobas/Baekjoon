import sys
from collections import deque


class DAG:
    def __init__(self, num_vertices: int):
        self.path = {i: [] for i in range(1, num_vertices + 1)}
        self.in_degree = [0] * num_vertices
        self.T = []

    def add_edge(self, u: int, v: int):
        self.path[u].append(v)
        self.in_degree[v - 1] += 1


def bfs(g: DAG, size: int) -> None:
    my_que = deque()
    visited = [False] * size

    for each in g.path:
        if g.in_degree[each - 1] == 0:
            my_que.append(each)

    while my_que:
      my_now = my_que.popleft()
      g.T.append(my_now)

      visited[my_now - 1] = True

      for my_next in g.path[my_now]:
          if not visited[my_next - 1]:
              g.in_degree[my_next - 1] -= 1

              if g.in_degree[my_next - 1] == 0:
                my_que.append(my_next)
    

if __name__ == "__main__":
    N, M = list(map(int, sys.stdin.readline().split()))
    g = DAG(N)

    for _ in range(M):
        A, B = list(map(int, sys.stdin.readline().split()))
        g.add_edge(A, B)
        
    bfs(g, N)

    for sorted_node in g.T:
        print(sorted_node)