init_data = [
    "###...#.###.###.#.#.###.###.###.###.###",
    "#.#...#...#...#.#.#.#...#.....#.#.#.#.#",
    "#.#...#.###.###.###.###.###...#.###.###",
    "#.#...#.#.....#...#...#.#.#...#.#.#...#",
    "###...#.###.###...#.###.###...#.###.###"
]

bulb_pos = {}
for num in range(10):
    temp = set()
    for i in range(5):
        for j in range(3):
            if init_data[i][num * 4 + j] == '#':
                temp.add((i, j))
    bulb_pos[num] = temp


def get_cur_bulb_pos(idx):
    _cur_bulb_pos = set()
    for i in range(5):
        for j in range(3):
            if matrix[i][idx * 4 + j] == '#':
                _cur_bulb_pos.add((i, j))
    return _cur_bulb_pos


N = int(input())
matrix = [[*input()] for _ in range(5)]
can_make_nums = [None] * N
total_cases = 1

for i in range(N):
    cur_can_make_nums = []
    cur_bulb_pos = get_cur_bulb_pos(i)
    for num in range(10):
        if cur_bulb_pos.issubset(bulb_pos[num]):
            cur_can_make_nums.append(num * (10 ** (N - i - 1)))

    can_make_nums[i] = cur_can_make_nums
    total_cases *= len(cur_can_make_nums)

if total_cases == 0:
    print(-1)
else:
    answer = 0
    for i in range(N):
        answer += sum(can_make_nums[i]) * total_cases // len(can_make_nums[i])
    print(answer / total_cases)
