N, M, K = map(int, input().split())
dp = [[1] * (M + 1) for _ in range(N + 1)]
for a in range(1, N + 1):
    for z in range(1, M + 1):
        dp[a][z] = dp[a - 1][z] + dp[a][z - 1]

if dp[N][M] < K:
    print(-1)
else:
    answer = []
    while N > 0 and M > 0:
        # A로 시작하는 문자의 개수
        start_a_cnt = dp[N - 1][M]

        # K가 작거나 같으면, A로 시작한다.
        if K <= start_a_cnt:
            answer.append('a')
            N -= 1
        # K가 더 크면, Z로 시작한다. K를 줄여줘야 함에 유의
        else:
            answer.append('z')
            M -= 1
            K -= start_a_cnt
    answer.append('a' * N + 'z' * M)
    print(''.join(answer))
