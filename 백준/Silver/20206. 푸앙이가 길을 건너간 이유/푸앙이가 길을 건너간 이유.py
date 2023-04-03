A, B, C = map(int, input().split())
x1, x2, y1, y2 = map(int, input().split())
if B == 0:
    x_pos = -C / A

    if x1 < x_pos < x2:
        print('Poor')
    else:
        print('Lucky')
else:
    y_pos1 = (-A * x1 - C) / B
    y_pos2 = (-A * x2 - C) / B

    if (y_pos1 <= y1 and y_pos2 <= y1) or (y_pos1 >= y2 and y_pos2 >= y2):
        print('Lucky')
    else:
        print('Poor')
