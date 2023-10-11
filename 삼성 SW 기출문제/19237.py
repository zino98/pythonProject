N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

directions = list(map(int, input().split()))

priorities = []
for i in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))

    priorities.append(temp)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

smell = [[[0,0]] * N for _ in range(N)]

def update_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 1:
                smell[i][j][1] -= 1

            if graph[i][j] != 0:
                smell[i][j] = [graph[i][j], K]


def shark_move():
    new_graph = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if graph[x][y] != 0:
                shark_direction = directions[graph[x][y] - 1]
                found = False

                for idx in priorities[graph[x][y] - 1][shark_direction - 1]:
                    nx = x + dx[idx-1]
                    ny = y + dy[idx-1]

                    if 0<= nx < N and  0<= ny < N: # 주위에 냄새가 없을 때
                        if smell[nx][ny][1] == 0:
                            directions[graph[x][y] - 1] = idx

                            if new_graph[nx][ny] == 0:
                                new_graph[nx][ny] = graph[nx][ny]

                            else:
                                new_graph[nx][ny] = min(graph[nx][ny], new_graph[nx][ny])

                            found = True
                            break

                if found:
                    continue

                for idx in priorities[graph[x][y] - 1][shark_direction - 1]: # 주위에 냄새 가득
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if smell[nx][ny][0] == graph[x][y]:  # 자신의 냄새가 있는 곳이라면
                            # 해당 상어 방향 변경
                            directions[graph[x][y] - 1] = idx
                            # 상어 이동시키기
                            new_graph[nx][ny] = graph[x][y]
                            break

    return new_graph

answer = 0
while True:
    update_smell()
    new_data = shark_move()
    data = new_data
    answer += 1

    check = True
    for i in range(N):
        for j in range(N):
            if data[i][j] > 1:
                check = False
    if check:
        print(answer)
        break

    # 1000초가 지날 때까지 끝나지 않았다면
    if answer >= 1000:
        print(-1)
        break