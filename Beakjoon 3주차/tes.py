nlist = [3, 1, 8, 2, 5]

def bacaktracking(nlist: list[int], idx: int, printlist: list[int] = []):
    
    printlist.append(nlist[idx])
    print(printlist)

    for i in range(idx + 1, len(nlist)):
        bacaktracking(nlist, i, printlist)
        printlist.pop()


bacaktracking(nlist, 0)