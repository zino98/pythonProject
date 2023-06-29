from collections import deque
import sys

N = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

graph = [[-1] * N for _ in range(N)]
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == -1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx,ny])


bfs(r1,c1)
print(graph[r2][c2])