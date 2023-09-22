import sys

l, c = map(int, sys.stdin.readline().split())
words = sorted(list(map(str, sys.stdin.readline().split())))
answer = []

def Sol(cnt, idx):

    if cnt == l:
        vo, co = 0, 0

        for i in range(l):
            if answer[i] in ['a', 'e', 'i', 'o', 'u']:
                co += 1

            else:
                vo += 1

        if co >= 2 and vo >= 1:
            print("".join(answer))


    for i in range(idx, c):
        answer.append(words[i])
        Sol(cnt + 1, idx + 1)
        answer.pop()

Sol(0,0)