N, M = map(int, input().split())
arr = [*map(int, input().split())]
prefix_sum = [0]
cnt = [0] * M

for n in arr:
    temp = (prefix_sum[-1] + n) % M
    prefix_sum.append(temp)
    cnt[temp] += 1

answer = cnt[0]
for m in range(M):
    answer += (cnt[m] - 1) * cnt[m] // 2
    
print(answer)
