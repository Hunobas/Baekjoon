import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    stickerMap = []

    for _ in range(T):
        n = int(input())
        stickerMap.append(list(map(int, input().split())))
        stickerMap.append(list(map(int, input().split())))

        dp1 = [stickerMap[0][0], stickerMap[1][0]]

        if n > 1:
            dp2 = [stickerMap[0][1], stickerMap[1][1]]
            for j in range(1, n - 3, 2):
                dp2[0] = max((stickerMap[0][j + 2] +
                                dp1[0]),
                                (stickerMap[0][j + 2]) +
                                (stickerMap[1][j + 1]) +
                                    dp1[0])
                dp2[1] = max((stickerMap[1][j + 2] +
                                dp1[1]),
                                (stickerMap[1][j + 2]) +
                                (stickerMap[0][j + 1]) +
                                    dp1[1])
        
        for j in range(0, n - 2, 2):
            dp1[0] = max((stickerMap[0][j + 2] +
                            dp1[0]),
                            (stickerMap[0][j + 2]) +
                            (stickerMap[1][j + 1]) +
                                dp1[0])
            dp1[1] = max((stickerMap[1][j + 2] +
                            dp1[1]),
                            (stickerMap[1][j + 2]) +
                            (stickerMap[0][j + 1]) +
                                dp1[1])

        if n % 2 == 0:
            dp1[0] += stickerMap[1][-1]
            dp1[1] += stickerMap[0][-1]
        else:
            dp2[0] += stickerMap[1][-1]
            dp2[1] += stickerMap[0][-1]

        print(max(dp1 + dp2))