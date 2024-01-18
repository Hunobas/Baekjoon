import sys

def qsort(a: list[int], left:int, right:int) -> None:
    if left >= right:
        return

    if a[left] > a[(left + right) // 2]:
        a[(left + right) // 2], a[left] = a[left], a[(left + right) // 2]

    if a[(left + right) // 2] > a[right]:
        a[(left + right) // 2], a[right] = a[right], a[(left + right) // 2]

    if a[left] > a[(left + right) // 2]:
        a[(left + right) // 2], a[left] = a[left], a[(left + right) // 2]

    a[(left + right) // 2], a[right - 1] = a[right - 1], a[(left + right) // 2]

    pl = left + 1
    pr = right - 2
    x = a[right - 1]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    qsort(a, pl, right)
    qsort(a, left, pr)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    nlist = []

    if 1 <= N <= 1000000:

        for _ in range(N):
            nthnum = int(sys.stdin.readline())

            if abs(nthnum) <= 1000000:
                nlist.append(nthnum)
        
        qsort(nlist, 0, len(nlist) - 1)

        for i in nlist:
            print(i)