import sys

input = sys.stdin.readline

N = int(input())
in_company = set()
for _ in range(N):
    name, log = input().split()
    if log == 'enter':
        in_company.add(name)
    if log == 'leave':
        in_company.remove(name)
print(*sorted(in_company, reverse=True), sep='\n')
