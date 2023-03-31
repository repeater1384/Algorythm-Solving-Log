import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    input()
    N = int(input())
    arr = [int(input()) for  _ in range(N)]
    print('YES' if sum(arr) % N == 0 else 'NO')