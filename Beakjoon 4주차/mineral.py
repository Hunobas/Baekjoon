import sys
from collections import deque


def caveUpdate(cave: list[str], cluster: list[tuple[int, int]], min_down: int) -> None:
    for x, y in cluster:
        cave[y] = cave[y][:x] + '.' + cave[y][x+1:]

    for x, y in cluster:
        cave[y + min_down] = cave[y + min_down][:x] + 'x' + cave[y + min_down][x+1:]


def mineralClustering(cave: list[str], target: tuple[int, int]):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    mineral_graph: dict[int, deque[tuple[int, int]]] = {}

    for i in range(4):
        X = target[0] + dx[i]
        Y = target[1] + dy[i]
        if (0 <= X < len(cave[0]) and 0 <= Y < len(cave) and cave[Y][X] == 'x'):
            # deque의 초기화로 튜플을 전달하고 싶다면 아래와 같이 deque([()])로 줄 것.
            mineral_graph[i] = deque([(X, Y)])

    for i in range(4):
        if i in mineral_graph.keys():
            cluster: list[tuple[int, int]] = []
            while mineral_graph[i]:
                curr_mineral = mineral_graph[i].popleft()
                cluster.append(curr_mineral)
                for j in range(4):
                    X = curr_mineral[0] + dx[j]
                    Y = curr_mineral[1] + dy[j]
                    if (0 <= X < len(cave[0]) and 0 <= Y < len(cave) and cave[Y][X] == 'x' and (X, Y) not in cluster):
                        mineral_graph[i].append((X, Y))
                        # curr_mineral의 값이 땅에 닿는 Y좌표(cave[-1])라 더 볼 필요가 없는 경우
                        if Y == len(cave) - 1:
                            mineral_graph[i] = None
                            cluster = None
                            break
            # 클러스터의 요소들 중 각 X 좌표 중 가장 작은(실제로는 큰) Y 값을 가진 요소들로 최소화   
            if cluster:
                min_down = float('inf')
                for x, y in cluster:
                    lift_down = 0
                    while y + lift_down + 1 < len(cave) and cave[y + lift_down + 1][x] == '.':
                        lift_down += 1
                        min_down = min(min_down, lift_down)

                caveUpdate(cave, cluster, min_down)


def throwSticks(cave: list[str], R: int, N: int, heights: list[int], turn: int = 0) -> None:
    for i in range(N):
        if 1 <= heights[i] <= R:
            Y = R - heights[i]
            X = 0

            if (i + turn) % 2 == 0:
                X = cave[Y].find('x')
                if X != -1:
                    cave[Y] = cave[Y][:X] + '.' + cave[Y][X+1:]
            else:
                X = cave[Y].rfind('x')
                if X != -1:
                    cave[Y] = cave[Y][:X] + '.' + cave[Y][X+1:]

            mineralClustering(cave, (X, Y))


if __name__ == "__main__":
    R, C = list(map(int, sys.stdin.readline().split()))
    cave = []

    for _ in range(R):
        caveRow = sys.stdin.readline().strip()
        cave.append(caveRow)

    N = int(sys.stdin.readline().strip())
    heights = list(map(int, sys.stdin.readline().split()))

    throwSticks(cave, R, N, heights)

    for caveRow in cave:
        print(caveRow)