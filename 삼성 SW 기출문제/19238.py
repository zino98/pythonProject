from collections import deque
N, M, cost = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

car_x, car_y = map(int, input().split())
passenger = [list(map(int, input().split())) for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 최단 경로
def bfs(car_x, car_y):
    visited = [[-1] * N for _ in range(N)]
    queue = deque()
    queue.append((car_x, car_y))
    visited[car_x][car_y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < N:

                if board[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

    return visited

def check_distance(visited, passenger):

    i = 0
    for start_x, start_y, dest_x, dest_y in passenger:
        passenger[i].append(visited[start_x - 1][start_y - 1])
        i += 1

    passenger.sort(key = lambda x: (-x[4], -x[0], -x[1]))

def Sol(car_x, car_y):
    global cost

    while passenger:
        visited = bfs(car_x-1, car_y-1)
        check_distance(visited, passenger)

        start_x, start_y, dest_x, dest_y, distance = passenger.pop()

        for temp in passenger:
            temp.pop()

        visited = bfs(start_x-1, start_y-1)
        distance2 = visited[dest_x-1][dest_y-1]
        car_x, car_y = dest_x, dest_y

        if distance == -1 or distance2 == -1:
            print(-1)
            return

        cost -= distance
        if cost < 0:
            break
        cost -= distance2
        if cost < 0:
            break
        cost += distance2 * 2

    if cost < 0:
        print(-1)
    else:
        print(cost)

Sol(car_x, car_y)

