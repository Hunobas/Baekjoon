import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sec, ty, tx = map(int, input().split())
visited = [[False] * M for _ in range(N)]
fy, fx = 0, 0
temp = board[0][0]
for y in range(N):
    for x in range(N):
        if board[y][x] != 0 and board[y][x] < temp:
            # temp = board[y][x]
            fy = y
            fx = x

# print(fy)
# print(fx)
# print(temp)
q = deque()
q.append((fy, fx))
time = 0
while q:
    if time == sec:
        print(board[ty][tx])
    cy, cx = q.popleft()
    for dir in range(4):
        ny = cy + dy[dir]
        nx = cx + dx[dir]
        if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
            board[ny][nx] = board[cy][cx]
            temp = board[0][0]
            time += 1
            visited[ny][nx] = True


    # else:







print(board)