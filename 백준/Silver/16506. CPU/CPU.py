def switch(key):
    dic = {}
    dic['ADD'] = '0000'
    dic['SUB'] = '0001'
    dic['MOV'] = '0010'
    dic['AND'] = '0011'
    dic['OR'] = '0100'
    dic['NOT'] = '0101'
    dic['MULT'] = '0110'
    dic['LSFTL'] = '0111'
    dic['LSFTR'] = '1000'
    dic['ASFTR'] = '1001'
    dic['RL'] = '1010'
    dic['RR'] = '1011'
    return dic.get(key,'ERROR')

def get_bin(num,digit):
    return str(bin(num))[2:].zfill(digit)

for _ in range(int(input())):
    array = input().split()
    opcode ,rN = array[0],list(map(int,array[1:]))

    onC = False
    if opcode[-1] == 'C':
        opcode = opcode[:len(opcode)-1]
        onC =True

    res = switch(opcode)
    if onC : res += '10'
    else : res +='00'

    res += get_bin(rN[0],3)+get_bin(rN[1],3)
    if onC:
        res += get_bin(rN[2],4)
    else:
        res += get_bin(rN[2],3)+'0'
    print(res)
