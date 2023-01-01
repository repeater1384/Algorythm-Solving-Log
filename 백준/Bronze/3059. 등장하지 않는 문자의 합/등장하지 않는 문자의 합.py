from string import ascii_uppercase

for _ in range(int(input())):
    orig = set(ascii_uppercase)
    data = set(input())
    print(sum(ord(c) for c in orig - data))
