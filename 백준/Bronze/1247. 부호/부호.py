import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    sum = 0
    for _ in range(N):
        sum += int(input())
    print('+'  if sum>0  else '0' if sum == 0 else '-')