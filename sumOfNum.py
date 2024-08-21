import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    numStr = input()[:-1]

    sum = 0
    if (N == len(numStr)):
        for numChar in numStr:
            sum += int(numChar)
    
    print(sum)