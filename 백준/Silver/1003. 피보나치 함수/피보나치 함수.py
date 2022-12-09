#import numpy as np
# list = np.array([[0,0] for _ in range(41)])
#numpy ver.
# def fibo(n):
#     if n<2:
#         list[n][n] = 1
#         return list[n]
#     else:
#         if np.array_equal(list[n],np.array([0,0])):
#             list[n] = fibo(n-1) + fibo(n-2)
#         return list[n]

list = [[0,0] for _ in range(41)]

def fibo(n):
    if n<2:
        list[n][n] = 1
        return list[n]
    else:
        if list[n] == [0,0]:
            list[n][0] = fibo(n-1)[0] + fibo(n-2)[0]
            list[n][1] = fibo(n-1)[1] + fibo(n-2)[1]
        return list[n]


for _ in range(int(input())):
    n = int(input())
    print(' '.join(map(str,fibo(n))))
