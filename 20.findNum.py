import sys

def binarySearch(a: list[int], findNum:int, left: int, right: int) -> int:
    if left > right:
        return -1
    
    mid = (left + right) // 2

    if a[mid] == findNum:
        return mid
    elif a[mid] < findNum:
        return binarySearch(a, findNum, mid + 1, right)
    elif a[mid] > findNum:
        return binarySearch(a, findNum, left, mid - 1)


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    if 1 <= N <= 100000:
        Nlist = list(map(int, sys.stdin.readline().split(" ")))
        sorted_Nlist = sorted(Nlist)

    M = int(sys.stdin.readline())

    if 1 <= M <= 100000:
        Mlist = list(map(int, sys.stdin.readline().split(" ")))

    if N == len(Nlist) and M == len(Mlist):

        for mth_num in Mlist:
            if binarySearch(sorted_Nlist, mth_num, 0, len(sorted_Nlist) - 1) == -1:
                print(0)
            else:
                print(1)