from itertools import combinations

N, K = map(int, input().split())
words = [input() for _ in range(N)]
if K < 5:
    print(0)
else:
    target = []
    for word in words:
        temp = 0
        for w in word:
            temp |= 1 << (ord(w) - 97)
        target.append(temp)

    answer = 0
    for comb in combinations(
            [2, 8, 16, 32, 64, 128, 512, 1024, 2048, 4096, 16384, 32768, 65536, 131072, 262144, 1048576, 2097152,
             4194304, 8388608, 16777216, 33554432], K - 5):
        bit = 532741
        for c in comb:
            bit += c
        cnt = 0
        for word in target:
            if word & bit == word:
                cnt += 1
        answer = max(answer, cnt)
    print(answer)
