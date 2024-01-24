import sys

min = [float("inf")]
max = [-float("inf")]

def dfs(calDict: dict, num_list: list[int], start: int, result: int) -> int:

    for i in range(4):

        if sum(calDict.values()) == 0:
            if result < min[0]:
                min[0] = result
            if result > max[0]:
                max[0] = result
                
            break

        else:
            
            if calDict[i] == 0:
                continue
            else:

                temp = result
                if i == 0:
                    temp += num_list[start]
                elif i == 1:
                    temp -= num_list[start]
                elif i == 2:
                    temp *= num_list[start]
                elif i == 3:
                    if temp < 0:
                         temp //= -num_list[start]
                         temp = -temp
                    else:
                        temp //= num_list[start]

                calDict[i] -= 1
                dfs(calDict, num_list, start + 1, temp)
                calDict[i] += 1


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    cal_list = list(map(int, sys.stdin.readline().split()))

    calDict = {}
    visited = []

    for i in range(4):
        calDict[i] = cal_list[i]

    dfs(calDict, num_list, 1, num_list[0])

    print(max[0])
    print(min[0])