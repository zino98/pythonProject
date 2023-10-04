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


