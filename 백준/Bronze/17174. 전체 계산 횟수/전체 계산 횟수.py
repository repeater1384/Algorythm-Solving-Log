N,M = map(int,input().split());r=0
while(N>0):r+=N;N//=M
print(r)