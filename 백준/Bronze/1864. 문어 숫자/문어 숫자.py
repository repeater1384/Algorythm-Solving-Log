data = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while True:
    s = input()
    if s == '#':
        break
    answer = 0
    for i in range(len(s)):
        answer += data[s[i]] * 8**(len(s)-i-1)
    print(answer)