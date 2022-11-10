N = int(input())
p, *data = map(int, input().split())

fac = [1] * (N + 1)
for i in range(1, N + 1):
    fac[i] = fac[i - 1] * i

if p == 1:
    K = data[0]
    num = [i for i in range(1, 21)]
    answer = []
    cur_idx = N - 1
    while cur_idx >= 0:
        cur_order = 0
        while K > fac[cur_idx]:
            K -= fac[cur_idx]
            cur_order += 1
        answer.append(str(num.pop(cur_order)))
        cur_idx -= 1
    print(' '.join(answer))
if p == 2:
    answer = 1
    used = [i for i in range(1, 21)]
    cur_idx = N - 1
    for d in data:
        answer += fac[cur_idx] * used.index(d)
        used.remove(d)
        cur_idx -= 1
    print(answer)
