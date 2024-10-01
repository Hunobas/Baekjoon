import sys


def PrintStar10Recursive(n: int, seed: list[str] = []) -> list[str]:
    if n == 1:
        return ["*"]

    nThree = n // 3

    seed = PrintStar10Recursive(nThree, seed)

    for j in range(nThree):
        seed[j] = seed[j] * 3
    for i in range(nThree, n):
        seed.append(seed[i % nThree])
        if nThree <= i < nThree * 2:
            seed[-1] = seed[-1][:nThree] + " " * nThree + seed[-1][nThree * 2 :]

    return seed


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    result = []

    result = PrintStar10Recursive(N, result)
    for row in result:
        print(row)
