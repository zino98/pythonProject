from collections import deque

def bfs():
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()

        if x == K:
            print(dist[x])
            path(x)
            break

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)
                move[nx] = x

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(''.join(map(str, arr[::-1])))

N, K = map(int, input().split())
dist = [0] * 100001
move = [0] * 100001

bfs()