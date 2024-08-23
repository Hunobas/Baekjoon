import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline

    inputStr = input().strip()
    if len(inputStr) > 100000:
        inputStr = inputStr[:100000]
    left = deque(inputStr)
    right = deque()
    M = int(input())

    for _ in range(M):
        command = list(input()[:-1].split())
        if command[0] == "L" and left:
            right.appendleft(left.pop())
        if command[0] == "D" and right:
            left.append(right.popleft())
        if command[0] == "B" and left:
            left.pop()
        if command[0] == "P":
            if len(left) + len(right) + len(command[1]) > 600000:
                command[1] = command[1][: 600000 - len(left) - len(right)]
            left.append(command[1])

    print("".join(left + right))
