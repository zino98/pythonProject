from collections import deque

def bfs():
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()

        if x == K:
            print(dist[x])
            break

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)


N, K = map(int, input().split())
dist = [0] * 100001

bfs()
