arr = [1,3]
n = int(input())
for _ in range(n-2):
    arr.append(arr[-1] + 2 * arr[-2])

print(arr[n-1]%10007)