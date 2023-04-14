def solve():
    def check_sqrt(_n):
        return int(_n ** .5) ** 2 == _n

    n = int(input())
    answer = 4
    if check_sqrt(n):
        answer = min(answer,1)
    else:
        for i in range(1, int(n ** .5) + 1):
            temp1 = n - i * i
            if check_sqrt(temp1):
                answer = min(answer,2)
            else:
                for j in range(1, int(temp1 ** .5) + 1):
                    temp2 = temp1 - j * j
                    if check_sqrt(temp2):
                        answer = min(answer,3)
    return answer


print(solve())
