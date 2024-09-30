import sys
import math

def GetDivisorNumInBkCriterion(Divisee: int, TrimNum: int) -> int:
    result = 0
    for i in range(1, math.isqrt(Divisee) + 1):
        if i ** 2 == Divisee and i <= TrimNum:
            result += 1
        elif Divisee % i == 0 and i <= TrimNum and Divisee // i <= TrimNum:
            result += 2
    return result

def IsBkLargerThanN(N: int, k: int, FinalDivisee: int, memo: dict[int: int]) -> bool:
    BkOrder = 0
    
    for Divisee in range(1, FinalDivisee + 1):
        if Divisee not in memo:
            memo[Divisee] = GetDivisorNumInBkCriterion(Divisee, N)
        BkOrder += memo[Divisee]
        if BkOrder >= k:
            return True

    return False

def FindBk(N: int, k: int) -> int:
    left = (k - 1) // 2 + 1
    right = k
    result = left

    memo = {}

    while left <= right:
        mid = (left + right) // 2
        if IsBkLargerThanN(N, k, mid, memo):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    k = int(input())

    print(FindBk(N, k))
