N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

box = []
for i in range(N):
    box.append(list(map(int, board[i])))

size = min(N,M)
def find_square(k):
    for i in range(N-k+1):
        for j in range(M-k+1):
            if box[i][j] == box[i][j+k-1] == box[i+k-1][j] == box[i+k-1][j+k-1]:
                return True


    return False

for k in range(size,0,-1):
    if find_square(k):
        print(k**2)
        break