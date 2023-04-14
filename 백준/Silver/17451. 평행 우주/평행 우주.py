planet_num = int(input())
plantes = [*map(int,input().split())]
min_var = plantes[-1]
for planet in reversed(plantes):
    if planet>=min_var:
        min_var = planet
    else:
        min_var = planet * (((min_var-1) // planet)+1)
print(min_var)