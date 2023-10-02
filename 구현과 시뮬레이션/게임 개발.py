N, M = map(int, input().split())

board = [[0] * M for _ in range(N)]  # 방문
x, y, dir = map(int, input().split())
board[x][y] = 1

array = [list(map(int, input().split())) for _ in range(N)] # 입력

dx = [-1,0,1,0]
dy = [0,1,0,-1]  # 북, 동, 남, 서

def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]

    if board[nx][ny] == 0 and array[nx][ny] == 0:
        board[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0

    else:
        turn_time += 1
        continue

    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]

        if array[nx][ny] == 0:
            x, y = nx, ny

        else:
            break

        turn_time = 0

print(count)