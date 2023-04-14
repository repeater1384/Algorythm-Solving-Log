a = [int(input()) for _ in range(int(input()))]
min = float('inf')
dif = [a[i+1] - a[i] for i in range(len(a)-1)]

def GCDofTwoNumbers(a, b): 
    while b != 0:  
        a, b = b, a % b  
    return a  

GCDarr = dif[0] 
for i in range(len(dif)):  
    GCDarr = GCDofTwoNumbers(GCDarr, dif[i])  

cnt = (a[-1] - a[0]) // GCDarr + 1
print(cnt - len(a))