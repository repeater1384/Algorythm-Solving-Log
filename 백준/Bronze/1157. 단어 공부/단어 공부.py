word = input().upper()
freq = [word.count(chr(c)) for c in range(ord('A'), ord('Z') + 1)]

maxfreq = max(freq)
if freq.count(maxfreq) == 1:
    print(chr(freq.index(maxfreq)+ord('A')))
else:
    print('?')