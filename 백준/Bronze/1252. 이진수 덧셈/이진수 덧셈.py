a, b = map(lambda x: x[::-1], input().split())

if len(a) < len(b): a, b = b, a

for _ in range(len(a) - len(b)):
    b += '0'

result = ''
carry = 0
for i in range(len(a)):
    cur = int(a[i]) + int(b[i]) + carry
    if cur >= 2:
        carry = 1
        result += str(cur - 2)
    else:
        carry = 0
        result += str(cur)
result += str(carry)
result = result[::-1]
print(result[result.find('1'):])
