N = int(input())
marble = [*map(int, input().split())]

marble_sum = sum(marble) + 1
# dp[i] => i번째 구슬까지 사용해서 만들수 있는 무게의 종류
dp = [set() for _ in range(N)]
dp[0].add(0)
dp[0].add(marble[0])
for i in range(1, N):
    cur = marble[i]
    dp[i] = dp[i - 1].copy()
    for temp in dp[i - 1]:
        for next in (temp - cur, cur, cur - temp, temp + cur):
            if next >= 0:
                dp[i].add(next)

M = int(input())
print(*['Y' if c in dp[N - 1] else 'N' for c in map(int, input().split())])
