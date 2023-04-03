price_weight = [[*map(int,input().split())] for _ in range(3)]
cost_effective_answer = [0,0]
answers= ['S','N','U']
for idx,priceNweight in enumerate(price_weight):
    price,weight = priceNweight
    all_price = price*10-500 if price >=500 else price*10
    cost_effective = weight*10/all_price
    if cost_effective>cost_effective_answer[0]:
        cost_effective_answer[0] = cost_effective
        cost_effective_answer[1] = idx

print(answers[cost_effective_answer[1]])