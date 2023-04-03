for _ in range(int(input())):
    k,s = input().split()
    print(s[:int(k)-1]+s[int(k):])