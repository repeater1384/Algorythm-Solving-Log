from datetime import datetime,timedelta
y1,m1,d1 = map(int,input().split())
y2,m2,d2 = map(int,input().split())
flag = 0
if m1<m2 or (m1==m2 and d1<=d2):
    flag = 1
만나이 = y2-y1-1+flag

세는나이 = y2-y1+1
연나이 = 세는나이-1
print(만나이,세는나이,연나이,sep='\n')
