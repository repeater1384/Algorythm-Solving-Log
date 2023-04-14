d, n = map(int, input().split())
oven = [*map(int, input().split())]
pizza = [*map(int, input().split())]

for i in range(1, d):
    oven[i] = min(oven[i], oven[i - 1])

oven = [*reversed(oven)]
pizza_idx = 0
oven_idx = 0
answer = 0
while oven_idx < len(oven) and pizza_idx < len(pizza):
    if oven[oven_idx] >= pizza[pizza_idx]:
        answer = len(oven) - oven_idx
        pizza_idx += 1
    oven_idx += 1

if pizza_idx == len(pizza):
    print(answer)
else:
    print(0)
