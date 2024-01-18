import sys
from collections import OrderedDict


# def wordSorting(slist: list[str], str_len: int) -> list[str]:
#     for _ in range(len(slist) - 1):
#         for i in range(len(slist) - 1, 0, -1):
#             for char in range(str_len):
#                 if ord(slist[i][char]) < ord(slist[i-1][char]):
#                     slist[i], slist[i-1] = slist[i-1], slist[i]
#                     break


def custom_sort(item):
    return (ndict[item], item)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    ndict = dict()

    if 1 <= N <= 20000:

        for _ in range(N):
            nthstr = sys.stdin.readline()

            if len(nthstr) <= 50:
                ndict[nthstr[:len(nthstr) - 1]] = len(nthstr) - 1

        sorted_dict = sorted(ndict, key=custom_sort)

        for nthstr in sorted_dict:
            print(nthstr)