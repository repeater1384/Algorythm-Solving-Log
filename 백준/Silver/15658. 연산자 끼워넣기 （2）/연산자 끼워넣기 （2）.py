N = input()
numbers = [*map(int, input().split())]
a, b, c, d = map(int, input().split())

max_val = float('-inf')
min_val = float('inf')


def cal(num, idx, add, sub, multi, divide):
    global max_val, min_val

    if idx == len(numbers):
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return
    if add:
        cal(num + numbers[idx], idx + 1, add - 1, sub, multi, divide)
    if sub:
        cal(num - numbers[idx], idx + 1, add, sub - 1, multi, divide)
    if multi:
        cal(num * numbers[idx], idx + 1, add, sub, multi - 1, divide)
    if divide:
        cal(int(num / numbers[idx]), idx + 1, add, sub, multi, divide - 1)


cal(num=numbers[0], idx=1, add=a, sub=b, multi=c, divide=d)

print(max_val)
print(min_val)
