# import sys

# def set(i: int, n: int) -> int:

#     case = 0

#     for j in range(n):
#         if(     not flag_a[j]
#             and not flag_b[i + j]
#             and not flag_c[i - j + n - 1]):
#             pos[i] = j
#             if i == n - 1:
#                 return 1
#             else:
#                 flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = True
#                 case += set(i + 1, n)
#                 flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = False

#     return case


# if __name__ == "__main__":

#     N = int(sys.stdin.readline())
#     pos = [0] * N
#     flag_a = [False] * N
#     flag_b = [False] * (2 * N - 1)
#     flag_c = [False] * (2 * N - 1)
#     case = set(0, N)

#     print(case)


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