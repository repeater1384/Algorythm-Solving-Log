for _ in range(int(input())):
    arr = [int(input()) for _ in range(int(input()))]
    if arr.count(max(arr)) == 1:
        if max(arr) > sum(arr) / 2:
            print('majority winner', arr.index(max(arr)) + 1)
        else:
            print('minority winner', arr.index(max(arr)) + 1)
    else:
        print('no winner')
