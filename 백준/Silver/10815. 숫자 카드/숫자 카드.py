input()
n_list=map(int,input().split())
input()
m_list=map(int,input().split())

n_count = {}
for n in n_list:
    n_count[n] = True

for m in m_list:
    try:
        a = n_count[m]
        print(1,end=' ')
    except:
        print(0,end=' ')