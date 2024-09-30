import sys

def CanCut(Lengthes: list[int], mid: int, n: int) -> bool:
    if mid == 0:
        return True

    cutNum = 0
    for Length in Lengthes:
        cutNum += Length // mid
        if cutNum >= n:
            return True
    return False

def FindMaxLAN(Lengthes: list[int], n: int) -> int:
    left = max(Lengthes) // n
    right = sum(Lengthes) // n
    result = left

    while left <= right:
        mid = (left + right) // 2
        if CanCut(Lengthes, mid, n):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result


if __name__ == "__main__":
    input = sys.stdin.readline

    K, N = list(map(int, input().split()))
    OriginalLANLengthes = []

    for _ in range(K):
        OriginalLANLengthes.append(int(input()))

    print(FindMaxLAN(OriginalLANLengthes, N))

    