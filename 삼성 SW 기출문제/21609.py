from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def find_block_group(x,y,num):

    rainbows = []
    blocks = [[x,y]]
    block_cnt, rainbow_cnt = 1, 0

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<= nx < N and 0<= ny < N and not visited[nx][ny] and board[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = 1
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append((nx,ny))

            if 0<= nx < N and 0<= ny < N and not visited[nx][ny] and board[nx][ny] == num:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                block_cnt += 1
                blocks.append((nx,ny))

    for r, c in rainbows:
        visited[r][c] = 0

    return block_cnt, rainbow_cnt, blocks + rainbows

def remove_block(arr):
    for r, c in arr:
        board[r][c] = -2


def gravity(arr):
    for i in range(N-2,-1,-1):
        for j in range(N):
            if arr[i][j] > -1:
                r = i
                while True:
                    if 0<= r+1 < N and arr[r+1][j] == -2:
                        arr[r+1][j] = arr[r][j]
                        arr[r][j] = -2
                        r += 1
                    else:
                        break


def rotation(arr) :
    temp = [[0] * N for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            temp[N-1-j][i] = arr[i][j]

    return temp

result = 0
while True:
    visited = [[0] * N for _ in range(N)]
    blocks = []

    for i in range(N):
        for j in range(N):

            if board[i][j] > 0 and visited[i][j] == 0:
                visited[i][j] = 1
                blocks_info = find_block_group(i,j,board[i][j])

                if blocks_info[0] >= 2:
                    blocks.append(blocks_info)

    blocks.sort(reverse=True)

    if not blocks:
        break
    remove_block(blocks[0][2])
    result += blocks[0][0] ** 2

    # 중력 작용
    gravity(board)
    # 90도 반시계 방향 회전
    board = rotation(board)
    # 다시 중력 작용
    gravity(board)

print(result)