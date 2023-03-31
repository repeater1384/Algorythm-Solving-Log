def check(data):
    idx = 0
    while idx < len(data):
        if data[idx:idx + 3] == '100':
            idx += 3
            while idx < len(data) and data[idx] == '0':
                idx += 1
            if idx == len(data):
                return 'NO'
            idx += 1
            while idx < len(data) and data[idx] == '1':
                if data[idx:idx + 3] == '100':
                    break
                else:
                    idx += 1
        elif data[idx:idx + 2] == '01':
            idx += 2
        else:
            return 'NO'
    return 'YES'


N = int(input())

for _ in range(N):
    print(check(input()))
