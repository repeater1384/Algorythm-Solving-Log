N, S = map(int, input().split())
numbers = [*map(int, input().split())]
cnt = 0


def dfs(idx, hap):
    global cnt
    if idx >= N:
        return

    hap += numbers[idx]
    if hap == S:
        cnt += 1
    dfs(idx+1,hap-numbers[idx])
    dfs(idx+1,hap)

dfs(0,0)
print(cnt)