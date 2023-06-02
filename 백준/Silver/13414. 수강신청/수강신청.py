import sys

input = sys.stdin.readline
K, L = map(int, input().split())

order = {}
success_list = [None] * L

for i in range(L):
    school_num = input().rstrip()
    if school_num in order:
        success_list[order[school_num]] = None
    order[school_num] = i
    success_list[i] = school_num

answer = []
idx = 0
while len(answer) < K and idx < L:
    cur = success_list[idx]
    if cur:
        answer.append(cur)
    idx += 1

print(*answer, sep='\n')
