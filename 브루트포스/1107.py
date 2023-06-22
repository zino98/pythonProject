import sys

def Sol():
    input = sys.stdin.readline
    N = int(input())
    num_of_broken = int(input())
    if num_of_broken != 0:
        broken = input().split()
    else:
        broken = []

    move_p_m = abs(100 - N)

    answer = 1000000
    for i in range(1000001):
        temp = move_p_m
        for j in list(str(i)):
            if j in broken:
                break
        else:
            temp = abs(i - N) + len(list(str(i)))
        answer = min(move_p_m, temp, answer)
    print(answer)


if __name__ == "__main__":
    Sol()

