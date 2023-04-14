dp1 = [0] * 3
dp2 = [0] * 3
temp1 = [0] * 3
temp2 = [0] * 3

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    temp1[0] = a + max(dp1[0], dp1[1])
    temp1[1] = b + max(dp1[0], dp1[1], dp1[2])
    temp1[2] = c + max(dp1[1], dp1[2])
    dp1 = temp1.copy()

    temp2[0] = a + min(dp2[0], dp2[1])
    temp2[1] = b + min(dp2[0], dp2[1], dp2[2])
    temp2[2] = c + min(dp2[1], dp2[2])
    dp2 = temp2.copy()

print(max(dp1), min(dp2))
