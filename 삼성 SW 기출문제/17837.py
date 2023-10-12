N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chess = [[[] for _ in range(N)] for _ in range(N)]
# 동 - 서 - 북 - 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
horse = []

for i in range(K):
    x, y, d = map(int, input().split())
    horse.append([x-1, y-1, d-1])
    chess[x-1][y-1].append(i)

count = 0

def change_dir(d):
    if d in [0, 2]:
        d += 1
    elif d in [1, 3]:
        d -= 1
    return d

def Sol(h_num):
    x, y, d = horse[h_num]
    nx = x + dx[d]
    ny = y + dy[d]

    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
        d = change_dir(d)
        nx = x + dx[d]
        ny = y + dy[d]
        horse[h_num][2] = d

        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
            return True

    horse_add = []
    for idx, number in enumerate(chess[x][y]):
        if number == h_num:
            horse_add.extend(chess[x][y][idx:])
            chess[x][y] = chess[x][y][:idx]
            break

    if board[nx][ny] == 1:
        horse_add = horse_add[-1::-1]

    for h in horse_add:
        horse[h][0], horse[h][1] = nx, ny
        chess[nx][ny].append(h)

    if len(chess[nx][ny]) >= 4:
        return False

    return True

while True:
    flag = False
    if count > 1000:
        print(-1)
        break

    for i in range(K):
        if Sol(i) == False:
            flag = True
            break
    count += 1

    if flag:
        print(count)
        break

