import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    RGBstrt = []

    for _ in range(N):
        RGBstrt.append(list(map(int, input().split())))

    if N != 2:
        for i in range(1, N):
            for j in range(3):
                RGBstrt[i][j] += min(RGBstrt[i - 1][(j + 1) % 3], RGBstrt[i - 1][(j + 2) % 3])

    print(min(RGBstrt[-1]))