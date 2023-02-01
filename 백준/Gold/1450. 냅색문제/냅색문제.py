N, C = map(int, input().split())
weight = [*map(int, input().split())]


def bisect_right(arr, x):
    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] <= x:
            s = m + 1
        else:
            e = m - 1
    return s


sum_a = [0]
sum_b = [0]

for i in range(N // 2):
    for j in range(len(sum_a)):
        sum_a.append(sum_a[j] + weight[i])
for i in range(N // 2, N):
    for j in range(len(sum_b)):
        sum_b.append(sum_b[j] + weight[i])
        
sum_a.sort()
sum_b.sort()

answer = 0
for b in sum_b:
    if b > C:
        break
    find = C - b
    cnt = bisect_right(sum_a, find)
    answer += cnt
    
print(answer)
