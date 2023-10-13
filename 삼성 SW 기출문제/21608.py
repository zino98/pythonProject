N = int(input())
students = [list(map(int, input().split())) for _ in range(N*N)]
room = [[0] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for order in range(N*N):
    student = students[order]

    tmp = []
    for i in range(N):
        for j in range(N):
           if room[i][j] == 0:
               like = 0
               blank = 0

               for k in range(4):
                   nx, ny = i + dx[k], j + dy[k]
                   if 0<= nx < N and 0<= ny < N:
                       if room[nx][ny] in student[1:]:
                           like += 1

                       if room[nx][ny] == 0:
                           blank += 1

               tmp.append([like, blank, i, j])

    tmp.sort(key= lambda x: (-x[0], -x[1], x[2], x[3]))
    room[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
## 점수를 매길 때는 학생 순서대로 점수 주기 위해 정렬함
students.sort()

for i in range(N):
    for j in range(N):
        ans = 0
        for k in range(4):
            nr, nc = i + dx[k], j + dy[k]
            if 0 <= nr < N and 0 <= nc < N:
                if room[nr][nc] in students[room[i][j]-1]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans-1)
print(result)