N, M = map(int, input().split())

P = sorted([int(input()) for _ in range(M)])

price = 0
total_price = 0
for i in range(M):
    temp = min(N, (M - i)) * P[i]
    if temp > total_price:
        price = P[i]
        total_price = temp
        
print(price, total_price)
