from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global a, b, c, total, visited
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()
        z = total - x - y

        if x == y == z:
            print(1)
            return

        for a, b in (x, y), (y, z), (z, x):
            if a > b:
                a = a - b
                b = b + b

            elif a < b:
                a = a + a
                b = b - a

            else:
                continue


            c = total - a - b
            x = min(a,b,c)
            y = max(a,b,c)

            if not visited[x][y]:
                visited[x][y] = -1
                queue.append((x,y))
    print(0)

a, b, c = map(int, input().split())
total = a + b + c
visited = [[-1] * (total + 1) for _ in range(total + 1)]

if total % 3 != 0:
    print(0)

else:
    bfs()