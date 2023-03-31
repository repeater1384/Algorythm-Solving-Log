for _ in range(int(input())):
    a=int(input())
    for _ in range(int(input())):
        b=[int(i) for i in input().split()]
        a+=b[0]*b[1]
    print(a)