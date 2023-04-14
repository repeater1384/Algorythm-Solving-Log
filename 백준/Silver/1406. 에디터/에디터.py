import sys

input = sys.stdin.readline

stack1 = [*input().strip()]
stack2 = []

for _ in range(int(input())):
    cmd = input()
    try:
        if cmd[0] == 'L':
            stack2.append(stack1.pop())
        if cmd[0] == 'D':
            stack1.append(stack2.pop())
        if cmd[0] == 'B':
            stack1.pop()
        if cmd[0] == 'P':
            stack1.append(cmd[2])
    except:
        continue
        
print(''.join(stack1 + stack2[::-1]))
