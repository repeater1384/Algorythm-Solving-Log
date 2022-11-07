N = int(input())
arr = sorted(map(int, input().split()))
MOD = 1_000_000_007
pow_list = [1]
for _ in range(N):
    pow_list.append(pow_list[-1] * 2 % MOD)

answer = 0
for i in range(N):
    answer = (answer + (pow_list[i] - pow_list[N - i - 1]) * arr[i]) % MOD
    
print(answer)
