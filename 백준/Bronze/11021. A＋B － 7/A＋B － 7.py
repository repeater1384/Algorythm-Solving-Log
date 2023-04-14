T = int(input())

for case in range(1, T+1):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print('Case #{}: {}'.format(case,a+b))