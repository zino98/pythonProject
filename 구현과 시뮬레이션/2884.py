clock = list(map(int,input().split()))

if clock[1] >= 45:
    clock[1] = clock[1] - 45
    print(*clock)

else:
    if clock[0] == 0:
        clock[0] = 23
        clock[1] = 60 - (45 - clock[1])
    else:
        clock[0] -= 1
        clock[1] = 60 - (45 - clock[1])
    print(*clock)