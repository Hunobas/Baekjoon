import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    total = input().strip()
    explodeStr = input().strip()

    while (index := total.find(explodeStr)) != -1:
        left = index - 1
        right = index + len(explodeStr)
        
        

    if total != "":
        print(total)
    else:
        print("FRLUA")
