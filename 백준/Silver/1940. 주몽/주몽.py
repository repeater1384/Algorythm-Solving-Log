N = int(input())
M = int(input())
arr = sorted(map(int, input().split()))

s, e = 0, N - 1
answer = 0
while s < e:
    cur = arr[s] + arr[e]
    if cur == M:
        s += 1
        e -= 1
        answer += 1
    elif cur > M:
        e -= 1
    else:
        s += 1
print(answer)
