import sys
from itertools import combinations

if __name__ == "__main__":
    input = sys.stdin.readline
    while (InputList := list(map(int, input().split()))) != [0]:
        k = InputList[0]
        S = set(InputList[1:])
        subsets = []

        for comb in combinations(S, k - 6):
            subsets.append(S - set(comb))
        for subset in subsets[::-1]:
            print(*subset)

        print()
