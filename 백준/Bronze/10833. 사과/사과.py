a=[]
for _ in range(int(input())):
    k = input().split()
    a.append(int(k[1])%int(k[0]))
print(sum(a))