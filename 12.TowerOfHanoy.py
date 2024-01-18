import sys


def printTowerOfHannoy(n: int, x: int, y: int, num: int = 0) -> None:
    if not (1 <= n <= 100):
        return
    
    printTowerOfHannoy(n - 1, x, 6 - x - y)
    print(f"{x} {y}")
    printTowerOfHannoy(n - 1, 6 - x - y, y)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    print(2 ** N - 1)

    if N <= 20:
        printTowerOfHannoy(N, 1, 3)
    ## **2^n은 O(1)이다. 하지만 다른 c^n 계산은 O(n)**
    