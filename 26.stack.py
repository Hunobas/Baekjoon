import sys
from collections import deque


def pop(my_que: deque) -> None:
    if len(my_que) == 0:
        print(-1)
    else:
        print(my_que.pop())

def push(my_que: deque, m: int) -> None:
    my_que.append(m)

def size(my_que: deque) -> None:
    print(len(my_que))

def empty(my_que: deque) -> None:
    if len(my_que) == 0:
        print(1)
    else:
        print(0)

def top(my_que: deque) -> None:
    if len(my_que) == 0:
        print(-1)
    else:
        print(my_que[-1])

doDict = {
    "pop": pop,
    "push": push,
    "size": size,
    "empty": empty,
    "top": top,
    }

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    my_que = deque()

    for _ in range(N):
        dolist = sys.stdin.readline().split(" ")
        if len(dolist) == 1:
            todo = dolist[0][:-1]
            doDict[todo](my_que)

        elif len(dolist) == 2:
            todo = dolist[0]
            M = int(dolist[1])
            doDict[todo](my_que, M)
        
