a = [int(input()) for _ in range(5)]
A = a[0]
B = a[1]
C = a[2]
D = a[3]
P = a[4]
x = P*A
y = B + max(0,(P-C)) * D
print(min(x,y))