from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
d = [(-1,0), (1,0), (0,-1), (0,1)]

result = 0
def bfs():
    queue = deque()
    test_graph = copy.deepcopy(graph)   #원본 데이터 그대로 복사, 훼손 X

    for i in range(N):
        for k in range(M):
            if test_graph[i][k] == 2:
                queue.append((i,k))

    while queue:
        x, y = queue.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y +dy
            if (0 <= nx < N) and (0 <= ny < M):
                if test_graph[nx][ny] == 0:
                    test_graph[nx][ny] = 2
                    queue.append((nx,ny))


    global result
    count = 0

    for i in range(N):
        for k in range(M):
            if test_graph[i][k] == 0:
                count += 1

    result = max(result, count)

def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(N):
        for k in range(M):
            if graph[i][k] == 0:
                graph[i][k] = 1
                make_wall(count+1)    # 재귀
                graph[i][k] = 0

make_wall(0)
print(result)