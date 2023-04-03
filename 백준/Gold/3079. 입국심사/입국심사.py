import sys

input = sys.stdin.readline


def get_passed_people(time, _Tk):
    return sum([time // k for k in _Tk])


N, M = map(int, input().split())
Tk = [int(input()) for _ in range(N)]

start, end = 0, max(Tk) * M

while start < end-1:

    mid = (start + end) // 2
    cur = get_passed_people(mid, Tk)
    if cur >= M:
        end = mid
    else:
        start = mid

print(end)
