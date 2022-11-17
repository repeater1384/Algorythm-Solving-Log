def solution(genres, plays):
    answer = []
    
    freq = {}
    num = 0
    for g,p in zip(genres,plays):
        if freq.get(g) == None:freq[g] = [(p,num)]
        else:freq[g].append((p,num))
        num += 1
        
    for _ ,v in sorted(freq.items(),key = lambda x : -sum([y[0] for y in x[1]])):
        v.sort(key=lambda x:-x[0])
        for _,a in v[:2]:
            answer.append(a)
    
    return answer