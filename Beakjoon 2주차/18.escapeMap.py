import sys
from collections import deque


def floodSpread(wQue: deque, map: list[str], R: int, C: int) -> bool:
    # 홍수 한 턴만 진행하기 위해 다음 턴 홍수 좌표 저장용 list 생성
    wTemps = []

    # 홍수 bfs
    while wQue:
        wEach = wQue.popleft()
        
        # 홍수 진행 (상/하/우/좌)
        for wEachX, wEachY in ((wEach[0] + 1, wEach[1]), (wEach[0] - 1, wEach[1]), (wEach[0], wEach[1] + 1), (wEach[0], wEach[1] - 1)):
            if 0 <= wEachX < R and 0 <= wEachY < C:
                if map[wEachX][wEachY] == '.' or map[wEachX][wEachY] == 'S':
                    map[wEachX][wEachY] = '*'
                    # 저장용 list에 다음 턴 홍수 좌표 담기
                    wTemps.append((wEachX, wEachY))

    # 한 턴 진행 후 while문 빠져나오고 다시 저장용 list으로부터 wQue에 담기
    wQue.extendleft(wTemps)


def bfs_mapEscape(sPos: tuple, wQue: deque, map: list, R: int, C: int) -> None:
    if map[sPos[0]][sPos[1]] != 'S':
        return

    sQue = deque()
    sQue.appendleft(sPos)
    tick = 0
    sTemps = []

    # 게임 오버 조건의 sQue
    while sQue:

        # sTemps에 이번 턴에 고슴도치가 생존한 위치 모두 담기
        while sQue:
            sTemps.append(sQue.popleft())

        # 시간 1분 진행
        tick += 1

        # 홍수 한 턴 진행
        floodSpread(wQue, map, R, C)

        # 고슴도치의 한 턴을 위한 bfs
        while sTemps:    
            sNow = sTemps.pop()

            # 고슴도치 도주 분기점 진행 (상/하/우/좌)
            for sNowX, sNowY in ((sNow[0] + 1, sNow[1]), (sNow[0] - 1, sNow[1]), (sNow[0], sNow[1] + 1), (sNow[0], sNow[1] - 1)):
                if 0 <= sNowX < R and 0 <= sNowY < C:
                    if map[sNowX][sNowY] == 'D':
                        print(tick)
                        return
                    elif map[sNowX][sNowY] == '.':
                        map[sNowX][sNowY] = 'S'
                        # 이번 턴에 sQue에 하나도 안 담긴다면 게임 오버
                        sQue.appendleft((sNowX, sNowY))

    # 게임 오버
    print("KAKTUS")


if __name__ == "__main__":
    R, C = list(map(int, sys.stdin.readline().split()))
    map = []
    Spos = (0, 0)
    WQue = deque()

    for row in range(R):
        mapRow = list(sys.stdin.readline()[:-1])
        map.append(mapRow)

        for col in range(C):
            if mapRow[col] == 'S':
                Spos = (row, col)
            elif mapRow[col] == '*':
                WQue.appendleft((row, col))
    
    bfs_mapEscape(Spos, WQue, map, R, C)