import math
from functools import reduce

N, S = map(int, input().split())
arr = [*map(lambda x: abs(int(x) - S), input().split())]
print(reduce(math.gcd, arr))
