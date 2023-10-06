import sys

input = sys.stdin.readline

N = int(input())
d = [0] * 301
s = [0] * 301

for i in range(N):
    s[i] = int(input())

d[0] = s[0]
d[1] = s[0] + s[1]
d[2] = max(s[0] + s[2], s[1] + s[2])

for i in range(3, N):
    d[i] = max(s[i] + d[i - 2], s[i] + s[i - 1] + d[i - 3])

print(d[N - 1])