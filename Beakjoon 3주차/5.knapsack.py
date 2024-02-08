import sys
from copy import deepcopy

if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = list(map(int, input().split()))
    luggage = []
    dp = [0] * (K + 1)

    for _ in range(N):
        W, V = list(map(int, input().split()))
        luggage.append((W, V))

    for i in range(N):
        dp_temp = deepcopy(dp)
        for j in range(1, K + 1):
            if j >= luggage[i][0]:
                dp[j] = max(dp_temp[j], luggage[i][1] + dp_temp[j-luggage[i][0]])

    print(dp[K])