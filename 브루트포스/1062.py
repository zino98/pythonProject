N, K = map(int, input().split())
words = [list(input()) for _ in range(N)] # 입력

letter = [False for _ in range(26)]  # 알파벳
answer = 0

for c in ('a', 'c', 'i', 'n', 't'):
    letter[ord(c) - ord('a')] = True # 방문 처리

def Sol(depth, cnt): # 백트래킹
    global answer

    if cnt == K-5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not letter[ord(w) - ord('a')]:
                    check = False
                    break
            
            if check:
                readcnt += 1

        answer = max(answer, readcnt)

    for i in range(depth, 26):
        if not letter[i]:
            letter[i] = True
            Sol(i, cnt+1)
            letter[i] = False