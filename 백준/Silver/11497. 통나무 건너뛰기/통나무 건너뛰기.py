for _ in range(int(input())):
    N = int(input())
    arr = [*map(int, input().split())]
    arr.sort()
    answer = 0
    for i in range(2, N):
        answer = max(answer, abs(arr[i] - arr[i - 2]))
    print(answer)
