N, K = map(int, input().split(' '))
coins = sorted([int(input()) for _ in range(N)], reverse=True)
answer = 0

for i in range(N):
    answer += K // coins[i]
    K %= coins[i]

print(answer)
