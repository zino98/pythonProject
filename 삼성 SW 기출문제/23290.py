from collections import deque
M, S = map(int, input().split())
board = [[0] * 4 for _ in range(4)]

fish = [[[[],[]]for _ in range(4)] for _ in range(4)]
for _ in range(M):
    fish_x, fish_y, fish_dir = map(int, input().split())
    fish[fish_x-1][fish_y-1][0].append(fish_dir-1)

shark_x, shark_y = map(int, input().split())
board[shark_x-1][shark_y-1] = 1

shark_x -= 1
shark_y -= 1

smell = [[0] * 4 for _ in range(4)]

d = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False] * 4 for _ in range(4)]

max_fish_cnt = -1
path = []

# 복제 시작
def copy_start():
    for i in range(4):
        for j in range(4):
            for dir in fish[i][j][0]:
                fish[i][j][1].append(dir)

# 물고기 이동
def move_fish():
    position = []
    for i in range(4):
        for j in range(4):

            while fish[i][j][0]:
                nd = fish[i][j][0].pop()
                flag = False
                for _ in range(8):
                    nx = i + d[nd][0]
                    ny = j + d[nd][1]
                    if (0<= nx < 4 and 0 <= ny < 4) and smell[nx][ny] == 0 and not (nx == shark_x and ny == shark_y):
                        position.append([nx,ny,nd])
                        flag = True
                        break

                    nd = (nd - 1) % 8

                if flag == False:
                    position.append([i,j,nd])

    return position

def select_move_shark(x, y, move_cnt, fish_cnt, temp_path):
    global shark_x, shark_y, max_fish_cnt, path, visited
    if move_cnt == 3:
        if max_fish_cnt < fish_cnt:
            max_fish_cnt = fish_cnt
            path = [d for d in temp_path]

        return

    for d in range(4):
        nx = shark_x + dx[d]
        ny = shark_y + dy[d]

        if 0<= nx < 4 and 0<= ny < 4:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                next_fish_cnt = fish_cnt + len(fish[nx][ny][0])
                select_move_shark(nx,ny,move_cnt+1,next_fish_cnt,temp_path+[d])
                visited[nx][ny] = False
            else:
                select_move_shark(nx,ny,move_cnt+1,fish_cnt,temp_path+[d])

def move_shark() :
    global shark_x, shark_y, fish, smell
    for d in path :
        shark_x = shark_x + dx[d]
        shark_y = shark_y + dy[d]
        if fish[shark_x][shark_y][0]:
            fish[shark_x][shark_y][0] = []
            smell[shark_x][shark_y] = 3 # 2가 아닌 3인 이유는 바로 다음 단계에서 1을 감소시키기 떄문

def reduce_smell() :
    global smell
    for i in range(4) :
        for j in range(4) :
            if smell[i][j] > 0 :
                smell[i][j] -= 1

def copy_end() :
    global fish
    for i in range(4) :
        for j in range(4) :
            while fish[i][j][1] :
                fish[i][j][0].append(fish[i][j][1].pop())


for now in range(S) :
    # 1. 복제 마법 시전 (물고기 복제)
    copy_start()
    # 2. 물고기 이동
    position = move_fish()
    for r, c, dir in position :
        fish[r][c][0].append(dir)

    path = []
    max_fish_count = -1

    # 3. 상어 이동
    select_move_shark(shark_x, shark_y, 0, 0, [])
    move_shark()

    # 4. 냄새 감소
    reduce_smell()
    # 5. 복제 완료
    copy_end()

result = 0
for i in range(4) :
    for j in range(4) :
        result += len(fish[i][j][0])

print(result)





