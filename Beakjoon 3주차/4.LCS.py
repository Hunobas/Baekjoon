import sys

# if __name__ == "__main__":
#     input = sys.stdin.readline
#     firS = input()[:-1]
#     secS = input()[:-1]

#     secStmp = secS
#     resultlist = []

#     dp = [[0] * (len(firS) + 1) for _ in range(len(secS) + 1)]
#     result = ""

#     for i in range(1, len(dp)):
#         for j in range(1, len(dp[0])):

#             dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

#             if secStmp[0] == firS[j - 1]:
#                 dp[i][j] += 1
#                 result += secStmp[0]
#                 secStmp = secStmp[1:]
        
#         secStmp = secS[i:]
#         resultlist.append(result)
#         result = ""

#     print(dp[len(secS)][len(firS)])


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
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    print(dp[len(secS)][len(firS)])