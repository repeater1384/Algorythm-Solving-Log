from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    prior = [(i,p) for i,p in zip(range(len(priorities)),priorities)]
    freq = {}
    for p in priorities:
        if freq.get(p) is None:
            freq[p] = 1
        else:
            freq[p] += 1
            
    freq = sorted(freq.items(),key = lambda x:-x[0])
    freq_idx = 0
    freq_cnt = 0
    order = []
    
    while freq_idx < len(freq):
        for i,p in prior:
            if freq_idx == len(freq) or freq[freq_idx][0] != p or i in order:
                continue
            order.append(i)
            if freq_cnt + 1 == freq[freq_idx][1]:
                freq_idx += 1
                freq_cnt = 0
            else:
                freq_cnt += 1
    return order.index(location)+1