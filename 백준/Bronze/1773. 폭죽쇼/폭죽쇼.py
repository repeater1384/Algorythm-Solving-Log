N, C = map(int, input().split())
time = [0] * (C + 1)
for _ in range(N):
    K = int(input())
    for i in range(K, C + 1, K):
        time[i] = 1
print(sum(time))
