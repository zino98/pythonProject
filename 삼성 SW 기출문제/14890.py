N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0

def check_line(line):
    for i in range(1,N):

        if abs(line[i] - line[i-1]) > 1:
            return False

        if line[i] < line[i-1]:
            for j in range(L):
                if i + j > N or visited[i] or line[i] != line[i+j]:
                    return False

                if line[i] == line[i+j]:
                    visited[i+j] = True

        elif line[i] > line[i-1]:
            for j in range(L):
                if i - j - 1 < 0 or visited[i] or line != line[i-j-1]:
                    return False

                if line[i] == line[i-j-1]:
                    visited[i-j-1] = True


for i in range(N):
    visited = [False for _ in range(N)]
    if check_line(board[i]):
        result += 1


for i in range(N):
    visited = [False for _ in range(N)]
    if check_line(board[j][i] for j in range(N)):
        result += 1

print(result)