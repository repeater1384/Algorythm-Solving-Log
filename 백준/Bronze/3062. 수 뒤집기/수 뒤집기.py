for _ in range(int(input())):
    N = int(input())
    temp = N + int(str(N)[::-1])
    print('YES' if str(temp) == str(temp)[::-1] else 'NO')
