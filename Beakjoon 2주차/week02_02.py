import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def mapBFS(map: list, start: tuple, size: int) -> int:
    if map[start[0]][start[1]] == "0":
        return 0
    
    cnt = 0
    inQue = deque()
    inQue.append(start)

    while inQue:
        inNow = inQue.popleft()
        x, y = inNow

        # visited 기능. 이미 방문한 집은 '0'으로 치환
        if map[x][y] == '0':
            continue
        map[x][y] = '0'
        
        cnt += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < size and 0 <= ny < size:
                if map[nx][ny] == "1":
                    inQue.append((nx, ny))

    return cnt


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    map = []
    # 단지(인덱스)와 각 단지의 집 개수
    housing = []

    # 맵 정보 입력
    for row in range(N):
        # map 변수 좌표값 찍기 쉬울려고 list[str]으로 받음
        mapRow = list(sys.stdin.readline()[:-1])
        map.append(mapRow)
    
    for i in range(N):
        for j in range(N):

            # N*N의 모든 좌표에 대해서 1인지 조사: 만약 1이면 BFS 진행, 0이면 바로 0 리턴
            if (housing_cnt := mapBFS(map, (i, j), N)) != 0:
                housing.append(housing_cnt)


    # 단지의 개수와 각 단지의 집 개수를 오름차순으로 출력
    print(len(housing))
    for housing_cnt in sorted(housing):
        print(housing_cnt)