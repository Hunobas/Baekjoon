import sys


def dfs(node: int, state: int, end: int, graph: list, dp: list) -> int:
    if state == end:
        if graph[node][0] != 0:
            return graph[node][0]
        else:
            return float("inf")
        
    if dp[node][state] != -1:
        return dp[node][state]

    dp[node][state] = float("inf")

    for i in range(N):
        if graph[node][i] == 0:
            continue

        dp[node][state] = min(dp[node][state], graph[node][i] + dfs(i, state or (1 << i), end, graph, dp))

    return dp[node][state]


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())

    graph = []
    dp = [[-1] * N for _ in range(1 << N)]

    for i in range(N):
        graph.append(list(map(int, input().split())))

    print(dfs(0, 1, (1 << N) - 1, graph, dp))