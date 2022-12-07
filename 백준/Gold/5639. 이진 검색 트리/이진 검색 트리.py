import sys
sys.setrecursionlimit(10**6)
arr = []
while True:
    try:
        arr.append(int(input()))
    except EOFError:
        break

answer = []


def dfs(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start, end):
        if arr[start] < arr[i + 1]:
            mid = i + 1
            break
    dfs(start + 1, mid - 1)
    dfs(mid, end)
    answer.append(arr[start])


dfs(0, len(arr) - 1)
print(*answer, sep='\n')
