N = int(input())
answer = 0
K = 1

while N > 0:
    if N < K:
        K = 1
    N -= K
    K += 1
    answer+=1

print(answer)