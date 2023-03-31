N = int(input())
A = [*map(int, input().split())]
dp1 = [0] * N

for i in range(N):
    temp = 0
    for j in range(i):
        if A[j] < A[i]:
            temp = max(temp, dp1[j])
    dp1[i] = temp + 1

A = A[::-1]
dp2 = [0] * N

for i in range(N):
    temp = 0
    for j in range(i):
        if A[j] < A[i]:
            temp = max(temp, dp2[j])
    dp2[i] = temp + 1

dp = [a + b - 1 for a, b in zip(dp1, dp2[::-1])]
print(max(dp))
