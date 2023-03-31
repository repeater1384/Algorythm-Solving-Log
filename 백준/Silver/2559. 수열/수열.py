n, k = map(int, input().split())
arr = [*map(int, input().split())]

cur = sum(arr[:k])
answer = cur
for i in range(k, n):
    cur = cur + arr[i] - arr[i-k]
    answer = max(cur, answer)
print(answer)
