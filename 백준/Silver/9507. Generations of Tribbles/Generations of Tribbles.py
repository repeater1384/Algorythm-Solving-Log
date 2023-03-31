d = [1,1,2,4]
while len(d)<68:
    d.append(d[-1]+d[-2]+d[-3]+d[-4])
for _ in range(int(input())):
    print(d[int(input())])