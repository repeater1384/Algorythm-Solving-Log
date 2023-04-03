from collections import deque

sieve = [True] * 10000

for i in range(2, 10000):
    if sieve[i]:
        for j in range(i + i, 10000, i):
            sieve[j] = False


def get_all_list_change_each_digit(num):
    all_list = []
    num = [*str(num)]

    for i in range(4):
        for j in range(10):
            if num[i] != str(j):
                new_num = int(''.join(num[:i] + [str(j)] + num[i + 1:]))
                if new_num >= 1000:
                    all_list.append(new_num)
    return all_list


for _ in range(int(input())):
    start, target = map(int, input().split())

    queue = deque([(start, 0)])
    visited = [False] * 10000
    visited[start] = True

    while queue:
        cur, cnt = queue.popleft()
        if cur == target:
            print(cnt)
            break
        for new in get_all_list_change_each_digit(cur):
            if not visited[new] and sieve[new]:
                queue.append((new, cnt + 1))
                visited[new] = True
