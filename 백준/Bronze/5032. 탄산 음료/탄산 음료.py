e, f, c = map(int, input().split())
cur = e + f
answer = 0
while cur >= c:
    a, b = divmod(cur, c)
    cur = a + b
    answer += a
print(answer)
