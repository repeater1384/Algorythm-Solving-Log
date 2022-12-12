N = int(input())
arr = [*map(int, input().split())]
arr.sort()
answer = 0
for i in range(N):
    s, e = 0, N - 1
    while s < e:
        if s == i:
            s += 1
        elif e == i:
            e -= 1
        else:
            cur = arr[s] + arr[e]
            if cur < arr[i]:
                s += 1
            elif cur > arr[i]:
                e -= 1
            else:
                answer += 1
                break
print(answer)
