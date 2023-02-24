max_val = float('-inf')
min_val = float('inf')
input()
inputNum = [*map(int, input().split())]
a, b, c, d = map(int, input().split())


def cal(num, idx, add, sub, multi, divide):
    global max_val, min_val, inputNum

    if idx == len(inputNum):
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return
    else:
        if add:
            cal(num + inputNum[idx], idx + 1, add - 1, sub, multi, divide)
        if sub:
            cal(num - inputNum[idx], idx + 1, add, sub - 1, multi, divide)
        if multi:
            cal(num * inputNum[idx], idx + 1, add, sub, multi - 1, divide)
        if divide:
            cal(int(num / inputNum[idx]), idx + 1, add, sub, multi, divide - 1)


cal(inputNum[0], 1, a, b, c, d)

print(max_val, min_val)
