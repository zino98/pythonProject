from collections import deque

# 입력, 보드
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 필요한 데이터 선언
shark_size = 2
now_x, now_y = 0
INF = 1e9

# 이동
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 아기 상어 초기값 저장
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            now_x, now_y = i, j
            board[i][j] = 0

# 아기 상어가 이동할 수 있는지
def BFS():
    visited = [[-1]*N for _ in range(N)]
    visited[now_x][now_y] = 0
    queue = deque()
    queue.append((now_x, now_y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:

                if shark_size >= board[nx][ny] and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


    return visited

# 아기 상어가 먹을 수 있는지
def Solve(visited):
    x, y = 0, 0
    min_distance = INF

    for i in range(N):
        for j in range(N):
            if visited[i][j] != -1 and 1 <= board[i][j] < shark_size:
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    x, y = i, j


    if min_distance == INF:
        return False

    else:
        return x, y, min_distance

answer = 0
food = 0

while True:
    result = Solve(BFS())

    if not result:
        print(answer)
        break

    else:
        now_x, now_y = result[0], result[1]
        answer += result[2]
        board[now_x][now_y] = 0
        food += 1

    if food >= shark_size:
        shark_size += 1
        food = 0