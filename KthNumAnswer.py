import sys


def CountNumbers(N: int, x: int) -> int:
    return sum(min(x // i, N) for i in range(1, N + 1))


def FindBk(N: int, k: int) -> int:
    left, right = 1, k

    while left <= right:
        mid = (left + right) // 2
        if CountNumbers(N, mid) < k:
            left = mid + 1
        else:
            right = mid - 1

    return left


N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

print(FindBk(N, k))
