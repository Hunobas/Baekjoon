import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    firS = input()[:-1]
    secS = input()[:-1]

    dp = [[0] * (len(firS) + 1) for _ in range(len(secS) + 1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if secS[i - 1] == firS[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[-1][-1])
    dx, dy = len(firS), len(secS)
    resS = ""

    while dx > 0 and dy > 0:
        if dp[dy - 1][dx] == dp[dy][dx]:
            dy -= 1
        elif dp[dy][dx - 1] == dp[dy][dx]:
            dx -= 1
        else:
            if firS[dx - 1] == secS[dy - 1]:
                resS = firS[dx - 1] + resS
                dx -= 1
                dy -= 1
    
    print(resS)