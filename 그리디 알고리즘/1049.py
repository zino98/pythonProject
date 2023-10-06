N, M = map(int, input().split())
price = [list(map(int, input().split())) for _ in range(M)]

six_price = sorted(price, key = lambda x : x[0])
one_price = sorted(price, key = lambda x : x[1])

result = 0

if six_price[0][0] > one_price[0][1] * 6:
    result += N * one_price[0][1]

else:
    result += (N // 6) * six_price[0][0]

    if (N % 6) * one_price[0][1] > six_price[0][0]:
        result += six_price[0][0]

    else:
        result += (N % 6) * one_price[0][1]

print(result)