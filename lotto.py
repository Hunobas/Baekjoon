import sys


def PrintAllLottoNumsRecursive(arr: list[int], start: int, current: list[int], depth):
    if depth == 6:
        print(*current)
        return

    for i in range(start, len(arr)):
        current.append(arr[i])
        PrintAllLottoNumsRecursive(arr, i + 1, current, depth + 1)
        current.pop()


if __name__ == "__main__":
    input = sys.stdin.readline
    while (InputList := list(map(int, input().split()))) != [0]:
        k = InputList[0]
        S = InputList[1:]
        PrintAllLottoNumsRecursive(S, 0, [], 0)
        print()
