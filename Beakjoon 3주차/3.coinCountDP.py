import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        N = int(input())
        coinlist = list(map(int, input().split()))
        M = int(input())

        dp = [0] * (M + 1)
        dp[0] = 1

        for i in range(N):
            for j in range(1, M + 1):
                if j >= coinlist[i]:
                    dp[j] += dp[j - coinlist[i]]

        print(dp[M])