input()
a, b = map(set, (input().split() for _ in range(2)))
print(len(a-b)+len(b-a))
