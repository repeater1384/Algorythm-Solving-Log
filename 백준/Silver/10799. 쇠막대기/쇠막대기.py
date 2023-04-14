k = list(input().replace('()','L'))
result = 0
curL = 0
while k:
    cur = k.pop(0)
    if cur == 'L':
        result += curL
    if cur == '(':
        curL += 1
    if cur ==')':
        curL -= 1
        result += 1
print(result)