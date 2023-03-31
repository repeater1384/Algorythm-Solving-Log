def gcd(a, b):
    a, b = max(a, b), min(a, b)

    while b:
        r = a % b
        a, b = b, r

    return a


for _ in range(int(input())):
    n, *nums = map(int, input().split())
    answer = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            answer += gcd(nums[i],nums[j])
    print(answer)
