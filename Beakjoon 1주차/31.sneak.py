import sys
from collections import deque


def turnHead(sneak: deque, LorD: str) -> str:
    ahead = [0, 0]

    print(sneak[-1])
    print(sneak[-2])
    
    ahead = [sneak[-1][0] - sneak[-2][0], sneak[-1][1] - sneak[-2][1]]
    if ahead == [0, 1]:
        if LorD == "L":
            return "LEFT"
        elif LorD == "D":
            return "RIGHT"
        
        return "UP"
    
    elif ahead == [0, -1]:
        if LorD == "L":
            return "RIGHT"
        elif LorD == "D":
            return "LEFT"
        
        return "DOWN"
    
    elif ahead == [1, 0]:
        if LorD == "L":
            return "UP"
        elif LorD == "D":
            return "DOWN"

        return "RIGHT"
    
    elif ahead == [-1, 0]:
        if LorD == "L":
            return "DOWN"
        elif LorD == "D":
            return "UP"
        
        return "LEFT"
    

def tick(n: int, sneak: deque, apples: list[list], turns: dict) -> int:
    i = 1
    j = 1
    tick = 0
    
    sneak.append([i, j])

    while (0 < sneak[-1][0] <= n) and (0 < sneak[-1][1] <= n):

        tick += 1

        # dir: 다음 틱 때 뱀이 향해야 하는 방향
        if tick in turns:
            dir = turnHead(sneak, turns[tick])
        else:
            dir = turnHead(sneak, None)

        if dir == "UP":
            j += 1
            sneak.append([i, j])
        elif dir == "DOWN":
            j -= 1
            sneak.append([i, j])
        elif dir == "LEFT":
            i -= 1
            sneak.append([i, j])
        elif dir == "RIGHT":
            i += 1
            sneak.append([i, j])
    
        for apple in apples:
            if [i, j] != apple:
                sneak.popleft()


        if sneak[-1] in sneak:
            break

    return tick


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    apples = []

    for _ in range(K):
        apple = list(map(int, sys.stdin.readline().split()))
        apples.append(apple)

    L = int(sys.stdin.readline())
    turns = {}

    for _ in range(K):
        sec, dir = sys.stdin.readline().split()
        turns[int(sec)] = dir

    sneak = deque()
    print(tick(N, sneak, apples, turns))
