N = int(input())

fibo = [1, 1]
for _ in range(40):
    fibo.append(fibo[-1] + fibo[-2])
    
print(fibo[N - 1], N - 2)
