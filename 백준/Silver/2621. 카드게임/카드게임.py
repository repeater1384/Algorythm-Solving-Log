# N = int(input())
#
# # balls = sorted([[*map(int, input().split()), i] for i in range(N)], key=lambda x: x[1])
#
# balls = [[*map(int, input().split()), i] for i in range(N)]
# answers = [0] * N
#
# for i in range(N):
#     color, size, index = balls[i]
#     for j in range(i):
#         if balls[j][0] != color:
#             answers[index] += balls[j][1]
#
# print(*answers,sep='\n')
def check_same_color(_colors, _numbers):
    temp = len(set(_colors))
    if temp == 1:
        return True, max(_numbers)
    return False, -1


def check_same_count(_numbers):
    _numbers = sorted(_numbers)
    freq = sorted([(i, _numbers.count(i)) for i in range(1, 10)], key=lambda x: x[1], reverse=True)
    if freq[0][1] == 4:
        return 4, freq[0][0]

    if freq[0][1] == 3:
        if freq[1][1] == 2:
            return 3.2, freq[0][0] * 10 + freq[1][0]

        return 3, freq[0][0]

    if freq[0][1] == 2:
        if freq[1][1] == 2:
            return 2.2, freq[1][0] * 10 + freq[0][0]

        return 2, freq[0][0]

    return 0, freq[4][0]


def check_straight(_numbers):
    _numbers = sorted(_numbers)
    temp = _numbers[0] - 1
    for num in _numbers:
        if temp + 1 != num:
            return False, -1
        temp = num
    return True, temp


colors = []
numbers = []
for _ in range(5):
    c, n = input().split()
    colors.append(c)
    numbers.append(int(n))

same_color, same_color_value = check_same_color(colors, numbers)
straight, straight_value = check_straight(numbers)
state, state_value = check_same_count(numbers)

if same_color:
    if straight:
        print(900 + straight_value)
    else:
        print(600 + same_color_value)
elif straight:
    print(500 + straight_value)
else:
    if state == 4:
        print(800 + state_value)
    if state == 3.2:
        print(700 + state_value)
    if state == 3:
        print(400 + state_value)
    if state == 2.2:
        print(300 + state_value)
    if state == 2:
        print(200 + state_value)
    if state == 0:
        print(100 + state_value)
