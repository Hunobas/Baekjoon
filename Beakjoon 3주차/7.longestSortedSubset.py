import sys

def longestSortedSubset(nlist: list[int], n: int) -> None:
    L = [1] * n

    for i in range(1, len(L)):
        subLongest = []

        for k in range(i):
            if nlist[k] < nlist[i]:
                subLongest.append(L[k])
                L[i] = 1 + max(subLongest)
    
    return max(L)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    nlist = list(map(int, sys.stdin.readline().split()))

    print(longestSortedSubset(nlist, N))