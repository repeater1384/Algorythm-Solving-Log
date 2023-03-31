t,q,c=map(int,input().split())

matrix =[[0]*(q+1) for _ in range(t+1)]
result = [[0,0,team] for team in range(t+1)]

for _ in range(c):
    time,t_n,q_n,re = input().split()
    time = int(time)
    t_n = int(t_n)
    q_n = int(q_n)

    if matrix[t_n][q_n] != -1:
        if re == 'AC':
            result[t_n][0] += time + matrix[t_n][q_n]*20  #결과 저장
            result[t_n][1] += 1
            matrix[t_n][q_n] = -1
        else:
            matrix[t_n][q_n] += 1

result = sorted(result[1:],key = lambda x:(-x[1],x[0],x[2]))
for team in result:
    print(team[2],team[1],team[0])