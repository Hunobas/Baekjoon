import sys
from collections import deque


if __name__ == "__main__":
    N = sys.stdin.readline()[:-1]
    my_que = deque()
    parent = 0
    bracket = 0