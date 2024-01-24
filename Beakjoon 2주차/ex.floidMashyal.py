import sys
from collections import deque


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    m = int(input())

    # 거리 배열 초기화
    distances = [[float("inf")] * n for _ in range(n)]
    for i in range (n):
        for j in range(n):
            if i == j:
                distances[i][j] = 0
    for _ in range(m):
        start, end, cost = list(map(int, sys.stdin.readline().split()))
        distances[start-1][end-1] = min(distances[start-1][end-1], cost)

    # 플로이드 와샬 알고리즘
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    # 답 출력
    for i in range (n):
        for j in range(n):
            if distances[i][j] == float("inf"):
                print(0, end=" ")
            else:
                print(distances[i][j], end=" ")
        print()