import sys

input = sys.stdin.readline
stack = [0]
ans = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    while stack[-1] > y:
        stack.pop()
        ans += 1
    if stack[-1] != y:
        stack.append(y)

ans += len(stack) - 1
print(ans)
