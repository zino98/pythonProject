# 최단경로 문제 -> BFS
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
move = [(1,0), (-1,0), (0,1), (0,-1)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

def bfs(a, b, wall_break_left):
    queue = deque()
    queue.append((a,b,wall_break_left))
    visited[a][b][wall_break_left]= 1

    while queue:
        x, y, wall_break_left = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][wall_break_left]

        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if board[nx][ny] == 0 and visited[nx][ny][wall_break_left] == 0:
                visited[nx][ny][wall_break_left] = visited[x][y][wall_break_left] + 1
                queue.append((nx,ny,wall_break_left))

            if board[nx][ny] == 1 and wall_break_left == 1:
                visited[nx][ny][wall_break_left - 1] = visited[x][y][wall_break_left] + 1
                queue.append((nx,ny,wall_break_left - 1))


    return -1

print(bfs(0,0,1))