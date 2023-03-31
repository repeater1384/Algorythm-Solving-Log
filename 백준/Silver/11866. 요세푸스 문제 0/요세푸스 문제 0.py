N,K = map(int,input().split())
stack = [i+1 for i in range(N)]
idx = 0
print('<',end='')
while len(stack)>1:
    idx+=K-1
    idx %= len(stack)
    print(stack.pop(idx),end=', ')
print(stack.pop(),'>',sep='')
