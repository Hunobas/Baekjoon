import sys


def SearchCardNum(Cards: list[int], Compare: int) -> bool:
    left, right = 0, len(Cards) - 1
    while left <= right:
        mid = (left + right) // 2
        if Cards[mid] == Compare:
            return True
        elif Cards[mid] < Compare:
            left = mid + 1
        else:
            right = mid - 1
    return False


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    Cards = list(map(int, input().split()))
    M = int(input())
    Compares = list(map(int, input().split()))

    Cards.sort()

    for Compare in Compares:
        if SearchCardNum(Cards, Compare):
            print(1, end=" ")
        else:
            print(0, end=" ")

    print()
