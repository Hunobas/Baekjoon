import sys


def separatedSum(num: int) -> int:
    sum = 0
    dividor = 10
    while num != 0:
        sum += num % dividor
        num //= dividor
    return sum


if __name__ == "__main__":
    input = sys.stdin.readline

    N = input()[:-1]
    numN = int(N)
    result = 0
    M = max(numN - len(N) * 9, 1)

    for i in range(M, numN):
        result = i + separatedSum(i)
        if result == numN:
            print(i)
            exit()

    print(0)
