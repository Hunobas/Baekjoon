import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())

    graph = [list(map(int, input().split())) for _ in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] != 0 and graph[k][j] != 0:
                    graph[i][j] = 1
    
    for g in graph:
        print(*g)