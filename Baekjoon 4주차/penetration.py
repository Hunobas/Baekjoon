import sys
from collections import deque


def penen_bfs(map: list[str], M: int, N: int) -> None:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    penen_que = deque()

    for mapX in range(N):
        if map[0][mapX] == "0":
            penen_que.append((0, mapX))
            map[0][mapX] = "-1"

    while penen_que:
        mapEach = penen_que.popleft()

        if mapEach[0] == M - 1:
            print("YES")
            exit()

        for i in range(4):
            mapX = mapEach[1] + dx[i]
            mapY = mapEach[0] + dy[i]

            if 0 <= mapX < N and 0 < mapY < M and map[mapY][mapX] == "0":
                penen_que.append((mapY, mapX))
                map[mapY][mapX] = "-1"

    print("NO")


if __name__ == "__main__":
    M, N = list(map(int, sys.stdin.readline().split()))
    map = []

    for _ in range(M):
        mapRow = list(sys.stdin.readline()[:-1])
        if len(mapRow) == N:
            map.append(mapRow)

    penen_bfs(map, M, N)
