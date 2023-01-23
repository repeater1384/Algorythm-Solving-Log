a = input()
if a[:2] == '0x':
    print(int(a, 16))
elif a[0] == '0':
    print(int(a, 8))
else:
    print(int(a))
