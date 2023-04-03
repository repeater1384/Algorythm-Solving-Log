N = int(input())
data = [*input()]
numbers = [int(input()) for _ in range(N)]
stack = []
for cur in data:
    if cur in ['+','-','*','/']:
        b = stack.pop()
        a = stack.pop()
        stack.append(eval(f'{a}{cur}{b}'))
    else:
        stack.append(numbers[ord(cur)-ord('A')])
print(f'{stack[0]:.2f}')