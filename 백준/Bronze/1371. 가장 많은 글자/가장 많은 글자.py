freq = [0] * 26
while True:
    try:
        for word in input().split():
            for w in word:
                freq[ord(w) - 97] += 1
    except EOFError:
        break

maxVal = max(freq)
for i in range(26):
    if freq[i] == maxVal:
        print(chr(i + 97), end='')
