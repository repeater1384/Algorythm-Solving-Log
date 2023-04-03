while True:
    x = input().lower()
    if x=='#':
        break
    print(x.count('a')+x.count('e')+x.count('i')+x.count('o')+x.count('u'))