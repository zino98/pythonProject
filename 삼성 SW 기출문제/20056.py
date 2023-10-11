N, M, K = map(int, input().split())
data = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    data[r-1][c-1].append([m,s,d])

direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(K):
    board = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if data[i][j] != []:

                for m,s,d in data[i][j]:
                    x = (i + direction[d][0] * s) % N
                    y = (j + direction[d][1] * s) % N

                    board[x][y].append([m,s,d])

    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                mass, speed, check1, check2 = 0, 0, 0, 0

                for m,s,d in board[i][j]:
                    mass += m
                    speed += s
                    if d % 2 == 0: check1 += 1
                    if d % 2 == 1: check2 += 1

                mass = mass // 5
                speed = speed // len(board[i][j])

                if mass == 0:
                    board[i][j] = []
                    continue

                if check1 == len(board[i][j]) or check2 == len(board[i][j]):
                    board[i][j] = []
                    for d in [0,2,4,6]:
                        board[i][j].append([mass, speed, d])

                else:
                    board[i][j] = []
                    for d in [1,3,5,7]:
                        board[i][j].append([mass, speed, d])

    data = [lst[:] for lst in board]


ans = 0
# 파이어볼이 있는 경우 질량 구하기
for i in range(N):
    for j in range(N):
        if data[i][j] != []:
            for m, s, d in data[i][j]:
                ans += m

print(ans)






