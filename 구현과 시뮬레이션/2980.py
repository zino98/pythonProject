N, M = map(int, input().split())
Time = 0
L = 0

for _ in range(N):
    D, R, G = map(int, input().split())
    Time += D - L
    L = D

    if Time % (R+G) <= R:
        Time += R - (Time % (R+G))


Time += M - L
print(Time)
