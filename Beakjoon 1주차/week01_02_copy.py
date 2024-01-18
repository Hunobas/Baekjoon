import sys

ans = []

def getSubsequence(s: int, nlist: list[int], start: int = 0) -> int:
    result = 0

    if sum(ans) == s and ans:
        return 1

    else:
        for i in range(start, len(nlist)):
            ans.append(nlist[i])
            getSubsequence(s, nlist, i + 1)
            ans.pop()

    return result


if __name__ == "__main__":
    n, s = list(map(int, sys.stdin.readline().split()))
    nlist = list(map(int, sys.stdin.readline().split()))

    if len(nlist) == n:
        print(getSubsequence(s, sorted(nlist)))