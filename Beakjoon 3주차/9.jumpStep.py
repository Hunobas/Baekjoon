import sys
from heapq import heapify, heappop
from math import inf

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = list(map(int, input().split()))
    passStone = []

    for _ in range(M):
        passStone.append(int(input()))

    dp = [[inf for _ in range(int((2 * N) ** (1/2)) + 2)] for _ in range(N)]
    dp[0][0] = 0
    acc = 2
    acc_con = acc + 1
    
    for i in range(1, N):

        acc_con -= 1
        if acc_con == 0:
            acc += 1
            acc_con = acc

        if (i + 1) in passStone:
            continue

        for j in range(1, acc):
            dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1

        print(f"{i + 1}번 돌: {dp[i]}")
        
    heapify(dp[-1])
    sol = heappop(dp[-1])

    if sol == inf:
        print(-1)
    else:
        print(sol)