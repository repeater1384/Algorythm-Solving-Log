import sys

input = sys.stdin.readline
N = int(input())
stack = []
answer = 0
for cur in [int(input()) for _ in range(N)]:
    while stack and cur >= stack[-1]:
        stack.pop()
    stack.append(cur)
    answer += len(stack) - 1
print(answer)
