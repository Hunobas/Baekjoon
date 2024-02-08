import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
q = deque()
sizes = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and board[i][j] == 1:
            q.append([i, j])
            visited[i][j] = True
            size = 0 

            while q:
                y, x = q.popleft()
                size += 1


                for dir in range(4):
                    ny = y + dy[dir]
                    nx = x + dx[dir]

                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and board[ny][nx] == 1:
                        q.append([ny, nx])
                        visited[ny][nx] = True

            sizes.append(size)
sizes.sort()
print(len(sizes))
for i in range(len(sizes)):
    print(sizes[i])