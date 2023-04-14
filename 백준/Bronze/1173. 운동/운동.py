N, m, M, T, R = map(int, input().split())

if m + T > M:
    print(-1)
else:
    answer = 0
    cur = m
    
    while N > 0:
        if cur + T <= M:
            cur += T
            N -= 1
        else:
            cur = max(cur - R, m)
        answer += 1

    print(answer)
