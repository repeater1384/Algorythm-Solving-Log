k = int(input())
list = sorted(list(map(int,input().split())))
sList = [sum(list[:i+1]) for i in range(k)]
print(sum(sList))