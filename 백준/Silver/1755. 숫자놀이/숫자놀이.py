data = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def num2str(n):
    if n < 10:
        return data[n]
    return ' '.join([data[n // 10], data[n % 10]])


M, N = map(int, input().split())
arr = []
for n in range(M, N + 1):
    arr.append([num2str(n), n])

arr.sort(key=lambda x: x[0])

try:
    for i in range((N - M + 1) // 10 + 1):
        for j in range(10):
            print(arr[i * 10 + j][1], end=' ')
        print()
except:
    pass
