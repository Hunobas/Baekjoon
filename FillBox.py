import sys


def FillBox(length: int, width: int, height: int, cubeList: dict[int:int]) -> int:
    result = 0
    for sideLen in list(cubeList.keys())[::-1]:
        boxSideLen = min(length, width, height)
        cubeNum = boxSideLen // sideLen
        if min(cubeList[sideLen], cubeNum) > 0:
            length -= cubeNum * sideLen
            width -= cubeNum * sideLen
            height -= cubeNum * sideLen
            cubeList[sideLen] -= cubeNum
            result += cubeNum
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    length, width, height = list(map(int, input().split()))
    N = int(input())
    cubeList = {}

    for _ in range(N):
        sideLen, cubeNum = list(map(int, input().split()))
        cubeList[sideLen] = cubeNum

    FillBox(length, width, height, cubeList)
