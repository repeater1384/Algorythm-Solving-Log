arr = [int(input()) for _ in range(10)]
temp = [sum(arr[:i]) for i in range(11)]
temp.sort(key=lambda x: (abs(100 - x), -x))
print(temp[0])
