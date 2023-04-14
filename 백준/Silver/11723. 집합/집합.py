import sys
S = set()
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == 'add':
        S.add(int(command[1]))
    if command[0] == 'remove':
        try:
            S.remove(int(command[1]))
        except:pass
    if command[0] == 'check':
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    if command[0] == 'toggle':
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            S.add(int(command[1]))
    if command[0] == 'all':
        S = set(range(1, 21))
    if command[0] == 'empty':
        S = set()
