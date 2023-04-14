N = int(input())

cities_length = [*map(int, input().split())]
price_per_liter = [*map(int, input().split())]

min_price_per_liter = price_per_liter[0]
answer = 0

for i in range(N - 1):
    min_price_per_liter = min(min_price_per_liter, price_per_liter[i])

    answer += min_price_per_liter * cities_length[i]

print(answer)