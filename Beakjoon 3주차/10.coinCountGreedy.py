import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = list(map(int, input().split()))
    coinlist = []

    for _ in range(N):
        coinlist.append(int(input()))

    cnt = 0

    for coin in coinlist[::-1]:
        if K < coin:
            continue
        elif K == 0:
            break
        cnt += K // coin
        K %= coin

    print(cnt)