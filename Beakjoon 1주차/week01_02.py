import sys
from collections import deque

resultlist = []

def getSubsequence(s: int, ndeque: deque) -> int:
    if len(ndeque) == 0:
        return 0
    
    result = 0

    if sum(ndeque) == s:
        if ndeque not in resultlist:
            result += 1
            resultlist.append(deque(ndeque))

    ltemp = ndeque.popleft()
    result += getSubsequence(s, ndeque)
    ndeque.appendleft(ltemp)

    if sum(ndeque) == s:
        if ndeque not in resultlist:
            result += 1
            resultlist.append(deque(ndeque))

    rtemp = ndeque.pop()
    result += getSubsequence(s, ndeque)
    ndeque.append(rtemp)

    return result


if __name__ == "__main__":
    n, s = list(map(int, sys.stdin.readline().split()))
    nlist = list(map(int, sys.stdin.readline().split()))
    ndeque = deque(sorted(nlist))

    if len(nlist) == n:
        print(getSubsequence(s, ndeque))
        print(resultlist)