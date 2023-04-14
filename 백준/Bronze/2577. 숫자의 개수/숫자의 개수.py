a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)
word = '0123456789'

for w in word:
    print(result.count(w))