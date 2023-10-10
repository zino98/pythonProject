N = int(input())
data = list(map(int, input().split()))
plus, sub, multiply, divide = map(int, input().split())

maximum = -1e9
minimum = 1e9

def Sol(idx, arr):
    global maximum, minimum, plus, sub, multiply, divide

    if idx == N:
        maximum = max(maximum, arr)
        minimum = min(minimum, arr)
        return

    else:
        if plus > 0:
            plus -= 1
            Sol(idx + 1, arr + data[idx])
            plus += 1

        if sub > 0:
            sub -= 1
            Sol(idx + 1, arr - data[idx])
            sub += 1

        if multiply > 0:
            multiply -= 1
            Sol(idx + 1, arr * data[idx])
            multiply += 1

        if divide > 0:
            divide -= 1
            Sol(idx + 1, int(arr / data[idx]))
            divide += 1

Sol(1, data[0])

print(maximum)
print(minimum)