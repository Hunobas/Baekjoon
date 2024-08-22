def printSumOfHiddenNum(n: int, mystr: str) -> None:
    if n != len(mystr):
        return

    sum = 0
    i = 0

    while i < len(mystr):
        if mystr[i] not in "0123456789":
            i += 1
        else:
            hiddenNum = "0"
            limit = 6
            while i < len(mystr) and mystr[i] in "0123456789" and limit != 0:
                hiddenNum += mystr[i]
                i += 1
                limit -= 1
            sum += int(hiddenNum)

    print(sum)


if __name__ == "__main__":
    n = int(input())
    mystr = input()

    printSumOfHiddenNum(n, mystr)
