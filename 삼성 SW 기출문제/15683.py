import copy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cctv_list = []
cctv_direction = [
        [],
        [[0], [1], [2], [3]], # 1번 CCTV
        [[0, 1], [2, 3]], # 2번 CCTV
        [[0, 2], [0, 3], [1, 2], [1, 3]], # 3번 CCTV
        [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # 4번 CCTV
        [[0, 1, 2, 3]] # 5번 CCTV
    ]

direction_list = [(1,0), (-1,0), (0,1), (0,-1)]
answer = 1e9

for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctv_list.append((i,j,board[i][j]))

def dfs(depth, graph):
    global answer

    if depth == len(cctv_list):
        answer = min(answer, check_zero(graph))
        return

    graph_copy = copy.deepcopy(board)
    x, y, cctv_type = cctv_list[depth]

    for cctv_dir in cctv_direction[cctv_type]:
        watch(x,y,cctv_dir,graph_copy)
        dfs(depth + 1, graph_copy)
        graph_copy = copy.deepcopy(board)

def watch(x,y,direction,graph):
    for d in direction:
        nx, ny = x, y

        while True:
            nx += direction_list[d][0]
            ny += direction_list[d][1]

            if 0<= nx < N and 0<= ny < M:

                if graph[nx][ny] == 6:
                    break

                elif graph[nx][ny] == 0:
                    graph[nx][ny] == '#'

            else:
                break

def check_zero(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1

    return cnt

dfs(0,board)
print(answer)