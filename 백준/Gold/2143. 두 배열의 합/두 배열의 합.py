import bisect

T = int(input())
N = int(input())
A = [*map(int, input().split())]
M = int(input())
B = [*map(int, input().split())]

prefix_A = [0]
prefix_B = [0]
for a in A:
    prefix_A.append(prefix_A[-1] + a)
for b in B:
    prefix_B.append(prefix_B[-1] + b)

can_A = []
for i in range(1, len(prefix_A)):
    for j in range(i):
        can_A.append(prefix_A[i] - prefix_A[j])

can_B = []
for i in range(1, len(prefix_B)):
    for j in range(i):
        can_B.append(prefix_B[i] - prefix_B[j])
can_A.sort()
can_B.sort()

answer = 0
for a in can_A:
    answer += bisect.bisect_right(can_B, T - a) - bisect.bisect_left(can_B, T - a)
print(answer)
