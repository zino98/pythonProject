from collections import deque

N, M = map(int, input().split())
board = [0] * 101
visited = [False] * 101

ladder = dict()
snake = dict()

for _ in range(N):
    a,b = map(int,input().split())
    ladder[a] = b

for _ in range(M):
    a,b = map(int, input().split())
    snake[a] = b

queue = deque()
queue.append(1)

while queue:
    x = queue.popleft()

    if x == 100:
        print(board[x])
        break

    for dice in range(1,7):
        next_x = x + dice

        if next_x <= 100 and not visited[next_x]:

            if next_x in ladder.keys():
                next_x = ladder[next_x]

            if next_x in snake.keys():
                next_x = snake[next_x]

            if not visited[next_x]:
                visited[next_x] = True
                board[next_x] = board[x] + 1
                queue.append(next_x)