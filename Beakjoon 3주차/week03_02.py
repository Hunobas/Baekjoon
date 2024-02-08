import sys
from heapq import heapify, heappop
from math import inf

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    board = []

    for _ in range(N):
        board.append(list(map(int, input().split())))

    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if dp[i][j] == 0 or (i == N - 1 and j == N - 1):
                continue

            jump = board[i][j]
            if 0 <= i + jump < N:
                dp[i + jump][j] += dp[i][j]
            if 0 <= j + jump < N:
                dp[i][j + jump] += dp[i][j]

    print(dp[-1][-1])