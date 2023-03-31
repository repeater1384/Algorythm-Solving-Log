def d_n(_n):
    return _n + sum(map(int, str(_n)))


result = [n for n in range(10001)]
for n in range(1, 10001):
    try:
        result[d_n(n)] = 0
    except:
        pass

print(*[n for n in result if n], sep='\n')
