import sys
list = [0] * int(input())
for i in range(len(list)):
    list[i] = int(sys.stdin.readline())
list.sort()
for i in list:
    print(i)