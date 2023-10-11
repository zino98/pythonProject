from collections import deque
N, M, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

food = [[5] * N for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, age = map(int, input().split())
    tree[r-1][c-1].append(age)

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def spring_summer():

    for i in range(N):
        for j in range(N):

            tree_cnt = len(tree[i][j])
            for k in range(tree_cnt):

                if food[i][j] >= tree[i][j][k]:
                    food[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1

                else:
                    for _ in range(k, tree_cnt):
                        food[i][j] += tree[i][j].pop() // 2

                    break

    return

def fall_winter():

    for i in range(N):
        for j in range(N):

            tree_cnt = len(tree[i][j])
            for k in range(tree_cnt):

                if tree[i][j][k] % 5 == 0:

                    for l in range(8):
                        nx = i + dx[l]
                        ny = j + dy[l]

                        if 0<= nx < N and 0<= ny < N:
                            tree[nx][ny].appendleft(1)

            food[i][j] += graph[i][j]

    return

for _ in range(K):
    spring_summer()
    fall_winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])

print(answer)





