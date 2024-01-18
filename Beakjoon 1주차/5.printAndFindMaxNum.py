import sys

def printAndFindMaxNum(a: list[int]) -> None:
    if not a:
        return

    maxIndex, maxNum = 1, a[0]

    for i in range(1, len(a)):
        if (a[i] > maxNum):
            maxNum = a[i]
            maxIndex = i + 1
    

    print(maxNum)
    print(maxIndex)


if __name__ == "__main__":
    a = []

    for i in range(9):
        temp = int(sys.stdin.readline())
        if not (0 < temp < 100):
            continue
        a.append(temp)
    
    printAndFindMaxNum(a)