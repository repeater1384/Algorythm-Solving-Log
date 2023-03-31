import sys

input = sys.stdin.readline
arr = [int(input()) for _ in range(int(input()))]

arr1 = [num for num in arr if num <= 0]
arr2 = [num for num in arr if num > 0]

arr1.sort()
arr2.sort(reverse=True)

answer = 0
if len(arr1) % 2 == 1:
    answer += arr1.pop()
if len(arr2) % 2 == 1:
    answer += arr2.pop()

while arr1:
    answer += arr1.pop() * arr1.pop()
while arr2:
    a, b = arr2.pop(), arr2.pop()
    answer += max(a * b, a + b)

print(answer)
