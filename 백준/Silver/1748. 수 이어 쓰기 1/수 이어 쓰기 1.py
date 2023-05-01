arr = [0]+[9*(10**i)*(i+1) for i in range(10)]

n = int(input())

digit = len(str(n))
answer = sum(arr[:digit]) + (n - 10**(digit-1) + 1)*digit
print(answer)