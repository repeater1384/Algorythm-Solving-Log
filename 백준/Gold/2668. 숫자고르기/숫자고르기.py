N = int(input())
arr = [int(input()) - 1 for _ in range(N)]

answer = set()


def dfs(start, cur, cycles, visited):
    if cycles and start == cur:
        for c in cycles:
            answer.add(c)
        return

    visited[cur] = True
    visited[start] = False
    if start == cur or not visited[arr[cur]]:
        dfs(start, arr[cur], cycles + [cur], visited)


for i in range(N):
    if i in answer:
        continue
    dfs(i, i, [], [False] * N)
answer = sorted(answer)
print(len(answer))
for i in answer:
    print(i+1)
