a,b,c = map(int,input().split())
d = int(input())

all = a*3600+b*60+c+d
sec = all%60
min = all//60%60%60
hour = all//3600%24
print(hour,min,sec)