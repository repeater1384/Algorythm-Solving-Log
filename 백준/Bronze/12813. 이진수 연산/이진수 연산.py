def not_op(_str):
    return ''.join('1' if b == '0' else '0' for b in _str)


a = int(input(), 2)
b = int(input(), 2)
print(bin(a & b)[2:].zfill(100000))
print(bin(a | b)[2:].zfill(100000))
print(bin(a ^ b)[2:].zfill(100000))
print(not_op(str(bin(a)[2:].zfill(100000))))
print(not_op(str(bin(b)[2:].zfill(100000))))
