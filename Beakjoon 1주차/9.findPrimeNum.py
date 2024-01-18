import sys
from math import sqrt


### 1 포함이 안되게 짤 것
def isPrime(n: int) -> bool:
    if (n == 1):
        return False
    
    for i in range(2, int(sqrt(n) + 1)):
        if (n % i == 0):
            return False
    return True


### 문제를 잘 읽을 것
def printPrimeNum(numList: list[int]) -> None:
    if len(numList) > 100:
        return
    
    ans = 0
    for num in numList:
        if not (0 < num <= 1000):
            return
        
        if (isPrime(num)):
            ans += 1
    
    print(ans)
        

if __name__ == "__main__":

    N = int(sys.stdin.readline())
    numList = list(map(int, sys.stdin.readline().split()))

    if (N == len(numList)):
        printPrimeNum(numList)