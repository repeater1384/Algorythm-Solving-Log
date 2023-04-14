n = int(input())/2
a = [*map(int,input().split())]
k = 1
for i in a:
    k*=i
print(round(k**(1/n)))