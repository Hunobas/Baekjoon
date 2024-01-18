import sys
from collections import deque

def binaryCompression(n: int, sec_array: list[list], comp_str: str) -> str:
    comp_str += "("

    
    binaryCompression(sec_array, comp_str)

    comp_str += ")"
    return


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    sec_array = []

    for _ in range(n):
        fir_array = list(map(int, sys.stdin.readline().split()))
        sec_array.append(fir_array)

    print(binaryCompression(n + 1, sec_array, ""))
    