def slope(building1, building2):
    return (building2[1] - building1[1]) / (building2[0] - building1[0])


N = int(input())
answer = 0
buildings = [*zip(range(1, N + 1), map(int, input().split()))]
for i in range(N):
    cur_building = buildings[i]
    left_buildings = buildings[:i][::-1]
    right_buildings = buildings[i + 1:]

    # 왼쪽 빌딩들 중에서, 내가 볼수 있는 빌딩의 개수
    # 기울기가 점점 작아져야 함.
    can_see_left = 0
    left_slope = float('inf')
    for left_building in left_buildings:
        temp_slope = slope(cur_building, left_building)
        if left_slope > temp_slope:
            can_see_left += 1
            left_slope = temp_slope

    # 오른쪽 빌딩들 중에서, 내가 볼수 있는 빌딩의 개수
    # 기울기가 점점 커져야 함.
    can_see_right = 0
    right_slope = -float('inf')
    for right_building in right_buildings:
        temp_slope = slope(cur_building, right_building)
        if right_slope < temp_slope:
            can_see_right += 1
            right_slope = temp_slope

    answer = max(answer, can_see_left + can_see_right)

print(answer)
