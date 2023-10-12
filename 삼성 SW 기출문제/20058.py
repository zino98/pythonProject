import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
ice_graph = [list(map(int, input().split())) for _ in range(2**N)]

L = list(map(int, input().split()))

#필요한 기본 정보
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 배열 회전
def turn(graph, L):
    new_graph = [[0]*(2**N) for _ in range(2**N)]

    for i in range(0,2**N,2**L):
        for j in range(0,2**N,2**L):
            for k in range(2**L):
                for m in range(2**L):
                    new_graph[i+m][j+(2**L - 1 - k)] = graph[i+k][j+m]

    return new_graph

def melt_ice(graph):
    new_graph = [[0] * (2**N) for _ in range(2**N)]

    for i in range(2**N):
        for j in range(2**N):

            ice_count = 0
            for dir in range(4):
                nx = i + dx[dir]
                ny = j + dy[dir]

                if 0<= nx < 2**N and 0<= ny < 2**N:
                    if graph[nx][ny] > 0:
                        ice_count += 1

            if ice_count < 3:
                new_graph[i][j] = graph[i][j] - 1

            else:
                new_graph[i][j] = graph[i][j]

    return new_graph

for i in range(Q):
    ice_graph = turn(ice_graph, L[i])
    ice_graph = melt_ice(ice_graph)


ice_sum = 0
max_size = 0
ice_check = [[False] * (2**N) for _ in range(2**N)]

for i in range(2**N):
    for j in range(2**N):

        if ice_check[i][j] == False and ice_graph[i][j] > 0:
            ice_sum += ice_graph[i][j]
            check = [[i,j]]
            ice_check[i][j] = True
            now_size = 1

            while check:
                x, y = check.pop(0)

                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]

                    if 0<= nx < 2**N and 0<= ny < 2**N:

                        if ice_check[nx][ny] == False and ice_graph[nx][ny] > 0:
                            ice_sum += ice_graph[nx][ny]
                            check.append([nx,ny])
                            ice_check[nx][ny] = True
                            now_size += 1


            max_size = max(max_size, now_size)

print(ice_sum)
print(max_size)
