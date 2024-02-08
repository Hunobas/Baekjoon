import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    mat_d = []

    d1, d2 = list(map(int, input().split()))

    mat_d.append(d1)
    mat_d.append(d2)
    
    for _ in range(1, N):
        _, d = list(map(int, input().split()))
        mat_d.append(d)

    dp = [[0] * N for _ in range(N)]

    # L: 행렬 간 곱셈 길이 ~ 2번 부터 N번 까지
    for L in range(2, N + 1):
        # N - L + 1: 이번 턴 곱셈 횟수
        for i in range(N - L + 1):
            j = i + L - 1
            dp[i][j] = float("inf")
            # k: dp 행렬의 대각선으로 가는 곱셈 번지수
            for k in range(i + 1, j + 1):
                dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k][j] + mat_d[i] * mat_d[k] * mat_d[j + 1])

    print(dp[0][N - 1])