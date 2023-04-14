a = list(input())
b = list(input())
i = 0
while i < len(a):
    if a[i] in b:
        b.remove(a[i])
        a.remove(a[i])
        i -= 1
    i += 1

print(len(a)+len(b))