a,d='',0
for i in[*zip(*[input()for _ in[0]*int(input().split()[0])])]:k=max('ACGT',key=lambda n:i.count(n));a+=k;d+=len(i)-i.count(k)
print(f'{a}\n{d}')