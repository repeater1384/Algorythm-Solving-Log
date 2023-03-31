a=input()
f=lambda x:a.count(x)
print(sum([f('a'),f('e'),f('i'),f('o'),f('u')]))