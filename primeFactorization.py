import sys
import math

def printFactorizedPrime(number: int) -> None:
    if (number == 1):
        return

    i = 2

    while (i <= math.sqrt(number)):
        if (number % i == 0):
            print(i)
            number //= i
        else:
            i += 1
    
    print(number)

if __name__ == "__main__":
    input = sys.stdin.readline

    number = int(input())
    printFactorizedPrime(number)