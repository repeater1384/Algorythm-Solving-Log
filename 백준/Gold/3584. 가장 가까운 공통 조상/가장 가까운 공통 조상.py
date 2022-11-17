import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    parents = [0] * (N + 1)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        parents[b] = a
        
    A, B = map(int, input().split())
    A_parents = [-1]
    B_parents = [-2]
    while parents[A]:
        A_parents.append(A)
        A = parents[A]
    A_parents.append(A)
    while parents[B]:
        B_parents.append(B)
        B = parents[B]
    B_parents.append(B)
    
    idx = -1
    while A_parents[idx] == B_parents[idx]:
        idx -= 1
    print(A_parents[idx + 1])
