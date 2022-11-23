arr = [float(input())for _ in range(10)]
arr.sort()
answer = 10 ** 9
for i in range(1,10):
    answer *= arr[i] / i
print(answer)