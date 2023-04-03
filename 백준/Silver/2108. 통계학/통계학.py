import sys
list = [int(sys.stdin.readline()) for _ in range(int(input()))]
list.sort()
s = sum(list)
l = len(list)
print(round(s/l))
print(list[l//2])
freq ={}
for i in list:
    if freq.get(i) == None:freq[i] = 1
    else:freq[i] += 1
m = max(freq.values())
mode =[]
for k,v in freq.items():
    if v==m:mode.append(k)
    if len(mode)==2:break
print(mode[-1])
print(list[-1]-list[0])