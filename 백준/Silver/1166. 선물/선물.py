N, L, W, H = map(int, input().split())

S, E = 0, max(L, W, H)
answer = 0
for _ in range(100):
    M = (S + E) / 2
    if (L // M) * (W // M) * (H // M) >= N:
        S = M
    else:
        E = M
print(M)
