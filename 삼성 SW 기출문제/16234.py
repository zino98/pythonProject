from collections import deque

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b):
    queue = deque()
    temp = []
    queue.append((a,b))
    temp.append((a,b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0 <= ny < N and visited[nx][ny] == -1:

                if L <= abs(country[x][y] - country[nx][ny]) <= R:
                    visited[nx][ny] = 0
                    queue.append((nx,ny))
                    temp.append((nx,ny))

    return temp

result = 0
while True:
    visited = [[-1] * N for _ in range(N)]
    flag = 0

    for i in range(N):
        for j in range(N):

            if visited[i][j] == -1:
                visited[i][j] = 0
                arr = bfs(i,j)

                if len(arr) > 1:
                    number = sum([country[x][y] for x, y in arr]) // len(arr)
                    flag = 1

                    for x,y in arr:
                        country[x][y] = number

    if flag == 0:
        break

    result += 1