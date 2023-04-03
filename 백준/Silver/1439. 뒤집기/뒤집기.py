data = input()+'.'

idx = 0
zero, one = [], []
while idx < len(data)-1:
    cur = 0
    for di in range(len(data) - idx):
        if data[idx] == data[idx + di]:
            cur += 1
        else:
            break
    if data[idx] == '0':
        zero.append(cur)
    elif data[idx] == '1':
        one.append(cur)
    idx += di
print(min(len(zero), len(one)))
