k = [int(input()) for _ in range(3)]
k.sort()
if sum(k) == 180:
    if k[-1] == 60:print('Equilateral')
    elif k[0] == k[1] or k[1] == k[2]:print('Isosceles')
    else:print('Scalene')
else:
    print('Error')