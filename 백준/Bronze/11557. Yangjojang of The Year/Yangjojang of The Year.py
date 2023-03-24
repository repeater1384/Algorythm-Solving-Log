T = int(input())
for _ in range(T):
    data = {}
    for k, v in [[*input().split()] for _ in range(int(input()))]:
        data[k] = data.get(k, 0) + int(v)
        
    max_v = -float('inf')
    answer = None
    
    for k, v in data.items():
        if v > max_v:
            max_v = v
            answer = k
    print(answer)
