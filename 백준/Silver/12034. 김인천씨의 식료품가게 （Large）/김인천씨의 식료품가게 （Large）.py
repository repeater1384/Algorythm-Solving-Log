T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [*map(int, input().split())]
    arr.sort()
    remain_numbers = arr.copy()
    answer = []
    for num in arr:
        if num in remain_numbers:
            remain_numbers.remove(num)
            remain_numbers.remove(num * 4 // 3)
            answer.append(num)
            
    print(f'Case #{tc}:', *answer)
