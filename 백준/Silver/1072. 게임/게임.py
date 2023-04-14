X, Y = map(int, input().split())

first_odds = int(Y *100 / X )

start, end = 1, 1000000000
answer = 0
while start <= end:
    mid = (start + end) // 2

    second_odds = int((Y + mid) * 100 / (X + mid))
    if first_odds < second_odds:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer if answer else -1)

