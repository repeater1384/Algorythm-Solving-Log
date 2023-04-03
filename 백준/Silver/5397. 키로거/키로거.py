def solve():
    data = input()
    stack1 = []
    stack2 = []
    for cmd in data:
        try:
            if cmd == '<':
                stack2.append(stack1.pop())
            elif cmd == '>':
                stack1.append(stack2.pop())
            elif cmd == '-':
                stack1.pop()
            else:
                stack1.append(cmd)
        except IndexError:
            continue

    return ''.join(stack1 + stack2[::-1])


for _ in range(int(input())):
    print(solve())