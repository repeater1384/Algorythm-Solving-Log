N = int(input())
arr = []


def is_good():
    for i in range(1, len(arr) // 2 + 1):
        if arr[-i:] == arr[-i * 2:-i]:
            return False
    return True


def back_tracking(depth):
    if not is_good():
        return False

    if depth == N:
        print(*arr, sep='')
        return True

    for next_num in [1, 2, 3]:
        arr.append(next_num)
        if back_tracking(depth + 1):
            return True
        arr.pop()


back_tracking(0)
