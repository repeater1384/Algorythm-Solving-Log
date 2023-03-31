from itertools import permutations

n = int(input())
numbers = [*map(int, input().split())]


def main_calculation(_numbers):
    temp = 0
    for i in range(len(_numbers) - 1):
        temp += abs(_numbers[i] - _numbers[i + 1])
    return temp


answer = float('-inf')
for p in permutations(numbers, n):
    answer = max(answer, main_calculation(p))
print(answer)
