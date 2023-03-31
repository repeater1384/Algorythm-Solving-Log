data = input()

stack = []
result = []

op1 = ['*', '/']
op2 = ['+', '-']

for char in data:
    if char == '(':
        stack.append(char)

    elif char == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()

    elif char in op1:
        if not stack:
            stack.append(char)
        else:
            while stack and stack[-1] in op1:
                result.append(stack.pop())
            stack.append(char)

    elif char in op2:
        if not stack:
            stack.append(char)
        else:
            while stack and stack[-1] in op1 + op2:
                result.append(stack.pop())
            stack.append(char)

    else:
        result.append(char)

while stack:
    result.append(stack.pop())

print(''.join(result))
