## 혼자서 시도, 실패
# import sys

# def nthQueen(n: int, fix_N:int, nlist: list[int]) -> int:
#     if len(nlist) == fix_N:
#         return 1
    
#     case = 0

#     for i in range(fix_N, 0, -1):
#         if nlist == []:
#             nlist.append(i)
#             case += nthQueen(n - 1, fix_N, nlist)
#             nlist.pop()
#             continue

#         if (i in nlist):
#             continue

#         temp = True
#         lenlist = len(nlist)
        
#         for j in range(lenlist):
#             if lenlist - j == abs(nlist[j] - i):
#                 temp = False

#         if temp:
#             nlist.append(i)
#             case += nthQueen(n - 1, fix_N, nlist)
#             nlist.pop()

#     return case


# if __name__ == "__main__":
#     N = int(sys.stdin.readline())
#     fix_N = N
#     case = 0
#     nlist = []

#     if 1 <= N <= 15:
#         case = nthQueen(N, fix_N, nlist)

#     print(case)


import sys

def set(i: int, n: int) -> int:

    case = 0

    for j in range(n):
        if(     not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + n - 1]):
            pos[i] = j
            if i == n - 1:
                return 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = True
                case += set(i + 1, n)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = False

    return case


if __name__ == "__main__":

    N = int(sys.stdin.readline())
    pos = [0] * N
    flag_a = [False] * N
    flag_b = [False] * (2 * N - 1)
    flag_c = [False] * (2 * N - 1)
    case = set(0, N)

    print(case)