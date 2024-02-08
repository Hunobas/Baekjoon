import sys

class Graph:
    def __init__(self, num_vertices: int):
        self.path = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u: int, v: int):
        self.path[u].append(v)
        self.path[v].append(u)

    
def countRowFloor(floors: list, rows: int, columns) -> int:
    result = 0

    for row in floors:
        column = 0

        for col in range(columns):
            while col < columns and row[col] == "|":
                col += 1

            while col < columns and row[col] == "-":
                col += 1

            result += 1
            



if __name__ == "__main__":
    N, M = list(map(int, sys.stdin.readline().split()))
    floors = []

    for _ in range(N):
        floors.append(list(sys.stdin.readline()[:-1]))
    