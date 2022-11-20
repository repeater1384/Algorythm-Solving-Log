def get_cnt(num):
    cnt = 0
    if num**.5 == int(num**.5):
        cnt -= 1
    for i in range(1,int(num**.5)+1):
        if num % i == 0:
            cnt += 2
    return cnt
def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        cnt = get_cnt(i)
        answer += power if cnt > limit else cnt
    return answer