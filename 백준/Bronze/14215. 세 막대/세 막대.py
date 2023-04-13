lines = [*map(int, input().split())]
lines.sort(reverse=True)
a, b, c = lines
while b + c <= a:
    a -= 1
print(a + b + c)
