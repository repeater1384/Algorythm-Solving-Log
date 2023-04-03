list = []
for i in range(7):
    k = int(input())
    if k%2:list.append(k)
if list:
    print(sum(list))
    print(min(list))
else:
    print(-1)