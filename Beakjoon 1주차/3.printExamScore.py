import sys

def printExamScore(a: int) -> None:
    if not (0 <= a <= 100):
        return
    
    if (a < 60):
        print("F")
    elif (a < 70):
        print("D")
    elif (a < 80):
        print("C")
    elif (a < 90):
        print("B")
    else:
        print("A")


if __name__ == '__main__':
    
    a = int(sys.stdin.readline())
    printExamScore(a)