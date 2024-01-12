import sys

def printOperations(a: int, b: int) -> None:
    if (a < 1 or a > 10000):
        return
    if (b < 1 or b > 10000):
        return
    
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)


if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().split())
    
    printOperations(a, b)