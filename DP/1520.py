import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1
    if dp[x][y] != -1:
    	return dp[x][y]
    else:
        dp[x][y] = 0
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] < graph[x][y]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))