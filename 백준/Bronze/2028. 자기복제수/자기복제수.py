for _ in range(int(input())):
    N = int(input())
    print('YES' if N == int(str(N * N)[::-1][:len(str(N))][::-1]) else 'NO')
