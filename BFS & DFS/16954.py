import sys
input = sys.stdin.readline
from collections import deque

# 맵 리스트, 벽 위치 조합, 정답 변수
board, wall, answer = [input().rstrip() for _ in range(8)], set(), 0

# 벽 위치 추가
for i in range(8):
    for j in range(8):
        if board[i][j] == '#':
            wall.add((i,j))

# 9가지 방향 정의
move = [[0, 0], [-1, 0], [1,0], [0,-1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
# 방문 표시 집합 생성, 매번 1초가 지날 때마다 업데이트 해야하므로 set 자료구조 사용한듯
visited = set()
# 큐 정의
queue = deque()
queue.append((7,0))

while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()
        if (x,y) in wall:
            continue

        if x == 0 and y == 7:
            answer = 1
            break

        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if 0 <= nx <= 7 and 0 <= ny <= 7 and not (nx,ny) in visited and not (nx,ny) in wall:
                visited.add((nx,ny))
                queue.append((nx,ny))

    if wall:
        visited = set()

    next_wall = set()
    for x, y in wall:
        if x < 7:
            next_wall.add((x+1, y))
    wall = next_wall

print(answer)