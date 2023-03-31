last_digits = {i: [i ** j % 10 for j in range(1, 5)] for i in range(1, 101)}

for _ in range(int(input())):
    a, b = map(int, input().split())
    answer = last_digits[a][b % 4 - 1]
    print(10 if answer == 0 else answer)
