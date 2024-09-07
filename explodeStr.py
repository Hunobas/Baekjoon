import sys


def canKeepExplodeStrRecuresive(
    total: str, startIndex: int, explodeStr: str
) -> tuple[bool, int]:
    endIndex = startIndex

    for targetC in explodeStr[1:]:
        if total[endIndex] != explodeStr[0] and total[endIndex + 1] == explodeStr[0]:
            canKeepExplode, endIndex = canKeepExplodeStrRecuresive(
                total, endIndex + 1, explodeStr
            )
            if not canKeepExplode:
                return (False, endIndex + 1)
        elif total[endIndex + 1] != targetC:
            return (False, endIndex + 1)
        else:
            endIndex += 1

    return (True, endIndex + 1)


if __name__ == "__main__":
    input = sys.stdin.readline

    total = input().strip()
    explodeStr = input().strip()

    compareCIndex = 0

    result = ""

    while compareCIndex < len(total):
        if total[compareCIndex] == explodeStr[0]:
            canExplode, endIndex = canKeepExplodeStrRecuresive(
                total, compareCIndex, explodeStr
            )
            if not canExplode:
                result += total[compareCIndex:endIndex]
            compareCIndex = endIndex
        else:
            result += total[compareCIndex]
            compareCIndex += 1

    if result == "":
        print("FRLUA")
    else:
        print(result)
