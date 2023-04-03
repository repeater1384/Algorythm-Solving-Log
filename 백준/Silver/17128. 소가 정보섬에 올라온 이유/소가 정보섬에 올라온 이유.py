import copy
N,Q = map(int,input().split())
cows = [*map(int,input().split())]
jangs = [*map(int,input().split())]

def cal(N,arr):
    temp = copy.deepcopy(arr)
    temp += temp[:3]
    result = 0
    for i in range(N):
        if i==0:
            cur = temp[0] * temp[1] * temp[2] * temp[3]
        else:
            cur = cur*temp[i+3]//temp[i-1]
        result += cur
    return result

def jangnan(hap,n):
    for i in range(-3,1):
        a = 1
        for j in range(4):
            if n+i+j >= N:
                # print(n+i+j-N,end='')
                a *= cows[n+i+j-N]
            else:
                # print(n+i+j,end='')
                a *= cows[n+i+j]
        # print()
        hap += 2*a
    return hap

hap = cal(N,cows)
for j in jangs:
    cows[j-1] = cows[j-1]*(-1)
    hap = jangnan(hap,j-1)
    print(hap)
