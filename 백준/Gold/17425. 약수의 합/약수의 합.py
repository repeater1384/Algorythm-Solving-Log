import sys

input = sys.stdin.readline


MAX = 1_000_001
dp = [0] * MAX
for i in range(1, MAX):
    for j in range(i, MAX, i):
        dp[j] += i

prefix_sum = [0]
for num in dp[1:]:
    prefix_sum.append(prefix_sum[-1] + num)
answer = []

for _ in range(int(input())):
    answer.append(prefix_sum[int(input())])
print(*answer, sep='\n')
