N = int(input())
rings = [*map(int, input().split())]


def get_gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


for ring in rings[1:]:
    gcd = get_gcd(rings[0], ring)
    print(f'{rings[0] // gcd}/{ring // gcd}')
