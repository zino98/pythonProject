T = int(input())

def Sol(n):

    if n == 1:
        return 1

    if n == 2:
        return 2

    if n == 3:
        return 4

    if n >= 4:
        return Sol(n-1) + Sol(n-2) + Sol(n-3)

for i in range(T):
    N = int(input())
    print(Sol(N))