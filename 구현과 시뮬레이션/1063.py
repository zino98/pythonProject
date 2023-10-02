king, stone, N = input().split()
k = list(map(int, [ord(king[0]) - 64, king[1]]))
s = list(map(int, [ord(stone[0]) - 64, stone[1]])) # 형변환

# 딕셔너리 활용
move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

for _ in range(int(N)):
    m = input()

    kx = k[0] + move[m][0]
    ky = k[1] + move[m][1]

    if 0 < kx <= 8 and 0 < ky <= 8:

        if kx == s[0] and ky == s[1]:
            sx = s[0] + move[m][0]
            sy = s[1] + move[m][1]

            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [kx, ky]
                s = [sx, sy]

        else:
            k = [kx, ky]

print(f'{chr(k[0] + 64)}{k[1]}')
print(f'{chr(s[0] + 64)}{s[1]}')
