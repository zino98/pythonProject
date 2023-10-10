from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def move(graph, dir):
    if dir == 0:
        edge = N - 1

        for i in range(N):
            for j in range(N-2,-1,-1):
                if graph[i][j]:
                    tmp = graph[i][j]
                    graph[i][j] = 0

                    if graph[i][edge] == tmp:
                        graph[i][edge] = 2 * tmp
                        edge -= 1

                    elif graph[i][edge] == 0:
                        graph[i][edge] = tmp

                    else:
                        edge -= 1
                        graph[i][edge] = tmp

    if dir == 1:
        edge = 0

        for i in range(N):
            for j in range(1,N):
                if graph[i][j]:
                    tmp = graph[i][j]
                    graph[i][j] = 0

                    if graph[i][edge] == tmp:
                        graph[i][edge] = 2 * tmp
                        edge += 1

                    elif graph[i][edge] == 0:
                        graph[i][edge] = tmp

                    else:
                        edge += 1
                        graph[i][edge] = tmp


    elif dir == 2:  # 남쪽
        for j in range(N):
            top = N - 1
            for i in range(N - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = tmp

    else:
        for j in range(N):
            top = 0
            for i in range(1, N):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = tmp

    return board

def dfs(board, cnt):
    global answer
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                answer = max(answer, board[i][j])
        return

    for i in range(4):
        tmp_board = move(deepcopy(board), i)
        dfs(tmp_board, cnt + 1)

dfs(board, 0)
print(answer)


