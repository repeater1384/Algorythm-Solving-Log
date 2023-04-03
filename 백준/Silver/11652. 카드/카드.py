import sys

input = sys.stdin.readline

freq = {}

for _ in range(int(input())):
    num = int(input())
    if freq.get(num) == None:
        freq[num] = 1
    else:
        freq[num] += 1

max_freq = max(freq.values())

temp = []
for k, v in freq.items():
    if v == max_freq:
        temp.append(k)

print(min(temp))