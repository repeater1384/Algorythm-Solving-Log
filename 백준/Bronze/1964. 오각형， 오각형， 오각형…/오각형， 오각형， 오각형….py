def get_penta_num_of_n(_n):
    # if _n == 1:
    #     return 5
    return (_n * (_n + 1)) * 3 // 2 + _n + 1


n = int(input())
print(get_penta_num_of_n(n) % 45678)