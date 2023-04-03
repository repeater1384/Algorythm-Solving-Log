n = int(input())
a, b = 0, 1
DIV = 1_000_000_007
for _ in range(n):
    a, b = b, (a + b) % DIV
print(a)
