import sys
from copy import deepcopy

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    stairSco = []
    dp = [[0] * (N + 1) for _ in range(2)]

    for _ in range(N):
        stairSco.append(int(input()))

    canSingleStp = True
    for i in range(1, N + 1):
        
        singtmp = dp[0][i-1]

        if i != 1:
            if dp[0][i - 2] + stairSco[i-1] <= dp[1][i - 2] + stairSco[i-1]:
                dp[1][i] = dp[1][i - 2] + stairSco[i-1]
            else:
                dp[1][i] = dp[0][i - 2] + stairSco[i-1]
                canSingleStp = True

        if canSingleStp:
            singtmp += stairSco[i-1]
            canSingleStp = False

        if not canSingleStp and i == N - 1:
            dp[0][i] = dp[0][i-1]
        else:
            if singtmp <= dp[1][i-1] + stairSco[i-1]:
                dp[0][i] = dp[1][i-1] + stairSco[i-1]
            else:
                dp[0][i] = singtmp


    print(max(dp[0][-1], dp[1][-1]))