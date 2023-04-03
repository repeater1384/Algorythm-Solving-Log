a,b = int(input()),input()
print(*[int(k)*a for k in b[::-1]],a*int(b),sep='\n')