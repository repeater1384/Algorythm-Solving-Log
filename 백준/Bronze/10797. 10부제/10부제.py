n=int(input())
a=map(int,input().split())
count=0
for i in a:
    if i==n:
       count+=1
print(count)