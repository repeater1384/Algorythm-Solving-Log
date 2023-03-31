a=int(input())
b=int(input())
a = a//100 *100
for k in range(a,a+100):
    if k%b == 0:
        print(str(k%100).zfill(2))
        break