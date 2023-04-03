def solution(budgets, M):
    start = 1
    end = max(budgets)

    while start <= end:
        s = 0
        mid = (start + end) // 2

        for b in budgets:
            s += min(b, mid)

        if s <= M:
            start = mid + 1
        else:
            end = mid - 1

    return end
input()
print(solution([*map(int,input().split())],int(input())))