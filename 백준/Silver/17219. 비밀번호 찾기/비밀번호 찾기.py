import sys
a,b = map(int,sys.stdin.readline().split())
passwords = {}
for _ in range(a):
    site,password=sys.stdin.readline().split()
    passwords[site] = password
for _ in range(b):
    print(passwords[sys.stdin.readline().strip()])