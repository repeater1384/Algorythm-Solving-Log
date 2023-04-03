input()
A = [*map(int, input().split())]
B = [*map(int, input().split())]
print(*sorted(A+B))