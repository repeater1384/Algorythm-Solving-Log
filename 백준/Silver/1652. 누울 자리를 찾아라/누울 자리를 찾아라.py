l=[input()for _ in[0]*(int(input()))]
f=lambda a:sum(sum('..'in c for c in b.split('X'))for b in a)
print(f(l),f(map(''.join,zip(*l))))