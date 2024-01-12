import sys
from math import sqrt


def isEven(n: int) -> bool:
    if (n % 2 == 1):
        return False
    else:
        return True


def isPrime(n: int) -> bool:
    if (n == 1):
        return False
    
    for i in range(2, int(sqrt(n) + 1)):
        if (n % i == 0):
            return False
    return True


def G_B_partition(n: int) -> None :
    if not (4 <= n <= 10000):
        return
    
    
    for i in range(n // 2, n):
        if (isPrime(n - i) and isPrime(i)):
            print(f"{n - i} {i}")
            break


if __name__ == "__main__":

    N = int(sys.stdin.readline())

    for _ in range(N):

        my_even = int(sys.stdin.readline())
        if (isEven(my_even)):
            G_B_partition(my_even)