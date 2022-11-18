import math
def solution(progresses, speeds):
    answer = []
    left = [math.ceil((100-p)/s) for p,s in zip(progresses,speeds)]+[1000]
    cur = left[0]
    conti = 1
    for i in range(1,len(left)):
        if cur >= left[i]:
            conti += 1
        else:
            answer.append(conti)
            cur = left[i]
            conti = 1
    return answer