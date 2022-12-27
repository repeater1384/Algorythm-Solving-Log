# old에서 new로 갈때 비용 계산, 같은 경우는 밖에서 처리함.
def get_cost(old, new):
    # 시작지점에서 출발
    if old == 0:
        return 2
    # 반대편으로 가는경우. 0으로 가는 경우가 있을까? ㄴㄴ
    if abs(old - new) == 2:
        return 4
    # 그외. 인접한 칸으로 가는 경우.
    return 3


arr = [*map(int, input().split())][:-1]
weight = {(0, 0): 0}
INF = float('inf')
for num in arr:
    next_weight = {}
    for key, val in weight.items():
        left, right = key
        if left == num or right == num:
            # 이미 발을 올려 놓았으면, +1
            next_weight[key] = min(next_weight.get(key, INF), val + 1)
        else:
            # 왼발이 num으로 움직이는 경우
            left_move = get_cost(left, num)
            next_weight[(num, right)] = min(next_weight.get((num, right), INF), val + left_move)
            # 오른발이 num으로 움직이는 경우
            right_move = get_cost(right, num)
            next_weight[(left, num)] = min(next_weight.get((left, num), INF), val + right_move)
    weight = next_weight
print(min(weight.values()))
