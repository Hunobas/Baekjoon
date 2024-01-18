import sys

def sortNums(nlist: list[int]) -> None:

    for _ in range(len(nlist) - 1):
        for i in range(len(nlist) - 1, 0, -1):
            if nlist[i] < nlist[i - 1]:
                nlist[i], nlist[i - 1] = nlist[i - 1], nlist[i]

    for n in nlist:
        print(n)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    nlist = []

    if 1 <= N <= 1000:

        for _ in range(N):
            nthnum = int(sys.stdin.readline())

            if abs(nthnum) <= 1000:
                nlist.append(nthnum)
        
        sortNums(nlist)