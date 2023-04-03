list = input().split('|')
C, A = 0, 0
for i in list:
    if i[0] == 'C' or i[0] == 'F' or i[0] == 'G':
        C += 1
    elif i[0] == 'A' or i[0] == 'D' or i[0] == 'E':
        A += 1

if C>A:
    print('C-major')
elif A>C:
    print('A-minor')
else:
    if list[-1][-1] == 'C' or list[-1][-1] == 'F' or list[-1][-1] == 'G':
        print('C-major')
    else:
        print('A-minor')
