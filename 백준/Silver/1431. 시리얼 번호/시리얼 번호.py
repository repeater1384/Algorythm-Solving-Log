N = int(input())
arr = [input() for _ in range(N)]
arr.sort(key=lambda x: (len(x), sum(int(y) for y in x if '0' <= y <= '9'), x))
print(*arr,sep='\n')
