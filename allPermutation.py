import sys

def PermutationRecursive(arr, used, current):
    if len(current) == len(arr):
        print(*current)
        return
    
    for i in range(len(arr)):
        if not used[i]:
            used[i] = True
            current.append(arr[i])
            PermutationRecursive(arr, used, current)
            used[i] = False
            current.pop()

if __name__ == "__main__":
    input = sys.stdin.readline
    
    N = int(input())
    arr = list(range(1, N + 1))
    used = N * [False]
    PermutationRecursive(arr, used, [])