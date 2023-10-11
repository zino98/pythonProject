import copy

N = 4
graph = [[None]*N for _ in range(N)]

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        graph[i][j] = [data[2*j], data[2*j+1]-1]

# 진행방향: 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
d = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

# (0, 0)에서 시작
shark_x = shark_y = 0
answer = 0

# 물고기 좌표
def find_fish(graph, fish):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == fish:
                return (i, j)


# 물고기 이동
def move_fish(shark_x, shark_y, graph):
    for fish in range(1, 17):
        position = find_fish(graph, fish)

        if position:
            fish_x, fish_y = position[0], position[1]
            direction = graph[fish_x][fish_y][1]

            for _ in range(len(d)):
                fish_nx = fish_x + d[direction][0]
                fish_ny = fish_y + d[direction][1]

                if 0<= fish_nx < N and 0<= fish_ny < N:

                    if not (fish_nx == shark_x and fish_ny == shark_y):
                        graph[fish_x][fish_y][1] = direction
                        graph[fish_x][fish_y], graph[fish_nx][fish_ny] = graph[fish_nx][fish_ny], graph[fish_x][fish_y]
                        break

                direction = (direction + 1) % len(d)


# 상어 이동
def move_shark(shark_x, shark_y, graph):
    direction = graph[shark_x][shark_y][1]
    position = []

    for _ in range(N-1):
        shark_x += d[direction][0]
        shark_y += d[direction][1]

        if 0<= shark_x < N and 0<= shark_y < N and graph[shark_x][shark_y][0] != -1:
            position.append((shark_x, shark_y))


    return position


# 재귀

def dfs(shark_x, shark_y, ate, graph):
    global answer
    graph = copy.deepcopy(graph)
    ate += graph[shark_x][shark_y][0]
    graph[shark_x][shark_y][0] = -1
    move_fish(shark_x, shark_y, graph)

    position = move_shark(shark_x, shark_y, graph)

    if position:
        for shark_nx, shark_ny in position:
            dfs(shark_nx, shark_ny, ate, graph)

    else:
        answer = max(answer, ate)
        return

dfs(shark_x, shark_y, 0, graph)
print(answer)