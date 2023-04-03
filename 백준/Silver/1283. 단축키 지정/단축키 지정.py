words = [input() for _ in range(int(input()))]
used = set()

for word in words:
    check = False
    splitedWord = [temp for temp in word.split()]

    for i in range(len(splitedWord)):
        temp = splitedWord[i]
        if temp[0] not in used:
            used.add(temp[0].lower())
            used.add(temp[0].upper())
            splitedWord[i] = splitedWord[i].replace(temp[0], '[' + temp[0] + ']', 1)
            check = True
            break

    if check:
        print(' '.join(splitedWord))
        continue

    findShort = None
    for temp in word.replace(' ', ''):
        if temp not in used:
            used.add(temp.lower())
            used.add(temp.upper())
            findShort = temp
            break

    if findShort is not None:
        print(word.replace(findShort, '[' + findShort + ']', 1))
        continue

    print(word)
