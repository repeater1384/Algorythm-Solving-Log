a, b, c = map(int, input().split())
op1, op2 = '', ''

if a + b == c:
    op1 = '+'
    op2 = '='
elif a - b == c:
    op1 = '-'
    op2 = '='
elif a * b == c:
    op1 = '*'
    op2 = '='
elif a / b == c:
    op1 = '/'
    op2 = '='
elif a == b + c:
    op1 = '='
    op2 = '+'
elif a == b - c:
    op1 = '='
    op2 = '-'
elif a == b * c:
    op1 = '='
    op2 = '*'
elif a == b / c:
    op1 = '='
    op2 = '/'

print(''.join(map(str, (a, op1, b, op2, c))))
