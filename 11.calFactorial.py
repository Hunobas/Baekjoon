import sys

def calFactorial(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * calFactorial(n - 1)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    print(calFactorial(N))