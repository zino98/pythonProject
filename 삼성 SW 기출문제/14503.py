
N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited[x][y] = 0
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        d = (d+3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if 0<= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            if visited[nx][ny] == -1:
                visited[nx][ny] = 0
                x, y = nx, ny
                flag = 1
                cnt += 1
                break

    if flag == 0:
        if board[x-dx[d]][y-dy[d]] == 1:
            print(cnt)
            break

        else:
            x, y = x - dx[d], y - dy[d]