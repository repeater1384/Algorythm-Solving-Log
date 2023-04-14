n,m = map(int,input().split())
pack = []
individual = []
for _ in range(m):
    p,i = map(int,input().split())
    pack.append(p)
    individual.append(i)
pack.sort()
individual.sort()
p = pack[0]
i = individual[0]
if i*6 < p:
    print(i*n)
else:
    print(min((n//6)*p + (n%6)*i,(n//6+1)*p))