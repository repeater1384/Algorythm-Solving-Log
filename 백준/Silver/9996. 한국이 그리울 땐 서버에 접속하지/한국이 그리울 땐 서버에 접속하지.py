n = int(input())
a,b = input().split('*')
for _ in range(n):
    text = input()
    if a == text[:len(a)]:
        text = text[len(a):]
        if b ==text[-len(b):]:print('DA')
        else:print('NE')
    else:print('NE')