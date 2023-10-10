import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]

INF = 1e9
res = INF

def Sol(M, idx):
    global res
    if M == N // 2:
        A, B = 0, 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += board[i][j]

                elif not visited[i] and not visited[j]:
                    B += board[i][j]

        res = min(res, abs(A-B))
        return

    for i in range(idx, N):
        visited[i] = True
        Sol(M+1, idx+1)
        visited[i] = False

Sol(0, 0)
print(res)