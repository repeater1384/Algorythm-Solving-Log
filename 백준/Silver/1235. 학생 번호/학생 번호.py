N=int(input())
s=[input()for _ in[0]*N]
k=1
while 1:
 if len({i[-k:]for i in s})==N:
  print(k)
  break
 k+=1