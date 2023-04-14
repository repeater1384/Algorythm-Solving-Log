#14717
def jockBo(num1,num2):
    if num1==num2:
        return '%dD'%num1
    else:
        return '%dG'%((num1+num2)%10)
def low_jockBo(jockBo):
    low = []
    if jockBo[-1] == 'D':
        for i in range(1,int(jockBo[:-1])):
            low.append('%dD'%i)
        for i in range(10):
            low.append('%dG'%i)
    elif jockBo[1] == 'G':
        for i in range(int(jockBo[0])):
            low.append('%dG'%i)
    return low
def BackTracking(deck,a,b):
    low = low_jockBo(jockBo(a,b)) #lower than my Combination[]
    all_time = 0
    victory_time = 0
    for i in range(0,len(deck)):
        for j in range(i+1,len(deck)):
            all_time += 1
            if jockBo(deck[i],deck[j]) in low:
                victory_time+=1
    return format(victory_time/all_time,'.3f')

deck = [i for i in range(1,11)]*2
a,b = map(int,input().split())
deck.remove(a),deck.remove(b)

print(BackTracking(deck,a,b))