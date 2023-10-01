N, M = map(int, input().split())
N_Ant = list[input()]
M_Ant = list[input()]
T = int(input())

N_Ant.reverse()
Total_Ant = N_Ant + M_Ant

for _ in range(T):
    for i in range(len(Total_Ant)-1):
        if Total_Ant[i] in N_Ant and Total_Ant[i+1] in M_Ant:
            Total_Ant[i], Total_Ant[i+1] = Total_Ant[i+1], Total_Ant[i]

            if Total_Ant[i+1] == N_Ant[-1]:
                break

print(''.join(Total_Ant))