N = int(input())
data = input()
b = data.count('b')
s = data.count('s')

if b > s:
    print('bigdata?')
elif b < s:
    print('security!')
else:
    print('bigdata? security!')
