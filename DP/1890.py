N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(N)]
direction = [(1,0), (0,1)]

def dfs(x,y):

    if x == N-1 and y == N-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    else:
        dp[x][y] = 0
        for d in direction:
            nx = x + d[0] * board[x][y]
            ny = y + d[1] * board[x][y]

            if 0 <= nx < N and 0 <= ny < N:
                dp[x][y] = dp[x][y] + dfs(nx,ny)

        return dp[x][y]

print(dfs(0,0))