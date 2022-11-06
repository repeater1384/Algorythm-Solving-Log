input()
arr = [*map(int, input().split())]
flag = int(input())

print(flag*sum([(a-1)//flag+1 for a in arr]))

