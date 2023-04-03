N, r, c = map(int, input().split())
answer = 0
while N > 0:
    temp = 2 ** (N - 1)
    if temp > r and temp > c:
        answer += temp * temp * 0

    elif r < temp <= c:
        answer += temp * temp * 1
        c -= temp

    elif c < temp <= r:
        answer += temp * temp * 2
        r -= temp

    elif temp <= r and temp <= c:
        answer += temp * temp * 3
        r -= temp
        c -= temp

    N -= 1

print(answer)