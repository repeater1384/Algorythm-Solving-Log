def get_gcd(a, b):
    if a % b == 0:
        return b
    return get_gcd(b, a % b)


def get_divsor(num):
    
    divsors = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            divsors.add(i)
            divsors.add(num // i)
    divsors.add(num)
    return sorted(divsors)


N = int(input())
numbers = sorted([int(input()) for _ in range(N)])

cur_gcd = numbers[1] - numbers[0]
for idx in range(2, N):
    cur_gcd = get_gcd(numbers[idx] - numbers[idx - 1], cur_gcd)

print(*get_divsor(cur_gcd))
