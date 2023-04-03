import string

N = int(input())
array = [' ']+list(string.ascii_uppercase)+list(string.ascii_lowercase)
keys = sorted(list(map(int,input().split())))
data = sorted(list(input()))
for i in range(N):
    if array[keys[i]] != data[i]:
        print('n')
        break
else:
    print('y')
