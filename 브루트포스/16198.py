import sys
input = sys.stdin.readline

N = int(input())

weight = list(map(int, input().split()))
max_Value = 0

def Sol(x):
    global max_Value

    if len(weight) == 2:
        max_Value = max(max_Value, x)
        return

    for i in range(1, len(weight) - 1):
        temp = weight[i-1] * weight[i+1]

        v = weight.pop(i)
        Sol(x+temp)
        weight.insert(i,v)

Sol(0)
print(max_Value)

