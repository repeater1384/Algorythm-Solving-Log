from collections import *
a=Counter(input())
print(*[a[chr(ord('a')+i)]for i in range(26)])