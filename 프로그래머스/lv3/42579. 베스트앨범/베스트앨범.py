def solution(genres, plays):
    freq = {}
    for g,p,num in zip(genres,plays,range(10001)):
        if freq.get(g) == None:freq[g] = [(p,num)]
        else:freq[g].append((p,num))
        
    return [a for _ ,v in sorted(freq.items(),key = lambda x : -sum([y[0] for y in x[1]])) for _,a in sorted(v,key=lambda x:-x[0])[:2]]