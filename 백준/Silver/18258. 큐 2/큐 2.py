import collections
import sys

input = sys.stdin.readline
que = collections.deque()
repeat = int(input())

for i in range(repeat):
    ins = input().rstrip().split(' ')

    if ins[0] == 'push':
        que.appendleft(ins[1])

    elif ins[0] == 'pop':
        if len(que) == 0:
            print("-1")
        else:
            print(que.pop())

    elif ins[0] == 'size':
        print(len(que))

    elif ins[0] == 'empty':
        if len(que) == 0:
            print("1")
        else:
            print("0")

    elif ins[0] == "front":
        if len(que) == 0:
            print("-1")
        else:
            print(que[len(que) - 1])

    elif ins[0] == "back":
        if len(que) == 0:
            print("-1")
        else:
            print(que[0])
