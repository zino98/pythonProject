R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if board[i][0] == -1:
        up = i
        down = i+1
        break

def spread():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    temp_board = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):

            if board[i][j] != 0 and board[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0<= nx < R and 0<= ny < C and board[nx][ny] != -1:
                        temp_board[nx][ny] += board[i][j] // 5
                        tmp += board[i][j] // 5

                board[i][j] -= tmp

    for i in range(R):
        for j in range(C):
            board[i][j] += temp_board[i][j]

def air_up():
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]

    x, y = up, 1
    before, direct = 0, 0

    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]

        if x == up and y == 0:
            break

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue

        board[x][y], before = before, board[x][y]
        x, y = nx, ny

def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        board[x][y], before = before, board[x][y]
        x = nx
        y = ny


for _ in range(T):
    spread()
    air_up()
    air_down()

answer = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            answer += board[i][j]

print(answer)

