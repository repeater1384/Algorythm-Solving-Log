N = int(input())
A = [*map(int, input().split())]

sorted_A = sorted(A)
result = []

for i in A:
    idx = sorted_A.index(i)
    result.append(idx)
    sorted_A[idx] = -1

print(*result)
